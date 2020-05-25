from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random
import numpy as np
from decimal import *

author = 'Anna'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'embez'
    players_per_group = 2
    num_rounds = 1
    k_min = 1
    k_max = 3
    k_step = 0.25
    endowment = 10
    tax_rate = .5
    total_taxes = players_per_group * endowment * tax_rate
    coef = .2
    checking_prob = .3
    K_CHOICES = list(np.arange(k_min, k_max + 0.01, k_step))
    K_CHOICES_STR = [float(round(i,2)) for i in K_CHOICES]
    fine_coef = 1.5

    correct_answers = dict(
        cq1_1=10,
        cq1_2=30,
        cq2_1=15,
        cq2_2=10,
        cq3_1=20,
        cq3_2=20,
    )


class Subsession(BaseSubsession):
    treatment = models.StringField()
    sign = models.BooleanField(initial=True)

    def creating_session(self):
        self.treatment = self.session.config.get('treatment')
        if self.treatment == 'negative':
            self.sign = False
        #  we give to each player some money at the beginning
        for p in self.get_players():
            p.endowment = Constants.endowment


class Group(BaseGroup):
    real_k = models.FloatField()
    k_declare = models.FloatField(
        widget=widgets.RadioSelectHorizontal,
        label='Выберите значение коэффициента, которое Вы объявите Гражданину:')

    def k_declare_choices(self):
        return [f'{i:.2f}' for i in Constants.K_CHOICES if i <= self.real_k]

    incentive = models.IntegerField()
    k_belief = models.FloatField(label='Как Вы думаете, чему был равен истинный коэффициент?',
                                 choices=Constants.K_CHOICES,
                                 widget=widgets.RadioSelectHorizontal, )
    taxes_paid = models.CurrencyField()
    taxes_multiplied = models.CurrencyField()
    taxes_paid_back = models.CurrencyField()
    individual_share = models.CurrencyField()
    embezzled_amount = models.CurrencyField(initial=0)
    officer_checked = models.BooleanField()
    true_k = models.BooleanField()
    officer_fine = models.CurrencyField()

    @property
    def officer(self):
        return self.get_player_by_role('officer')

    def after_group_is_formed(self):
        # in each period in each group an official is checked with certain probability.
        # we also generate a certain K based on which official can declare his own K
        r = random.random()
        g = self
        g.officer_checked = r < Constants.checking_prob
        g.real_k = random.choice(Constants.K_CHOICES)

    def apply_sanctions(self):
        """Applying sanctions on officer if he is checked.
        The officer payoff is diminished by the embezzled amount IF he is checked.
        """
        self.officer_fine = self.embezzled_amount * Constants.fine_coef
        self.officer.payoff -= self.officer_checked * self.true_k * self.officer_fine

    def set_payoffs(self):
        # we get two user (officer and citizen)
        officer = self.officer
        citizen = self.get_player_by_role('citizen')
        # we check if officer lied
        self.true_k = self.real_k == self.k_declare
        # collect all paid taxes
        self.taxes_paid = sum([p.tax_paid for p in self.get_players()])
        self.taxes_multiplied = self.taxes_paid * self.real_k;
        self.taxes_paid_back = self.taxes_paid * self.k_declare;
        # calculate how much everone one get based on amount declared by officer
        self.individual_share = self.taxes_paid_back / Constants.players_per_group
        # calculated an embezzled amount
        self.embezzled_amount = self.taxes_multiplied - self.taxes_paid_back
        for p in self.get_players():
            p.payoff = p.endowment - p.tax_paid + self.individual_share
        # this is for the treatment

        officer.payoff += self.embezzled_amount
        # apply punishment on the officer (if any):
        self.apply_sanctions()


class Player(BasePlayer):
    endowment = models.CurrencyField()
    tax_paid = models.CurrencyField()
    cq1_1 = models.IntegerField(label='Какое вознаграждение в этом периоде получает Гражданин?')
    cq1_2 = models.IntegerField(label='Какое вознаграждение в этом периоде получает Чиновник?')
    cq2_1 = models.IntegerField(label='Какое вознаграждение в этом периоде получает Гражданин?')
    cq2_2 = models.IntegerField(label='Какое вознаграждение в этом периоде получает Чиновник?')
    cq3_1 = models.IntegerField(label='Какое вознаграждение в этом периоде получает Гражданин?')
    cq3_2 = models.IntegerField(label='Какое вознаграждение в этом периоде получает Чиновник?')

    def role_desc(self):
        """return Russian description of role - for showing at the pages"""
        descs = dict(officer='Чиновник',
                     citizen='Гражданин')
        return descs.get(self.role())

    def role(self):
        """defines that the first player in group will be a bureaucrat"""
        if self.id_in_group == 1:
            return 'officer'
        return 'citizen'
