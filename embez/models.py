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

author = 'Your name here'

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
    coef = .2
    checking_prob = .3
    K_CHOICES = list(np.arange(k_min, k_max, k_step))
    fine_coef = 1.5

    correct_answers = dict(
        cq1_1=30,
        cq1_2=30,
        cq2_1=21,
        cq2_2=31,
        cq3_1=9,
        cq3_2=10,

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
        # in each period in each group an official is checked with certain probability.
        # we also generate a certain K based on which official can declare his own K
        for g in self.get_groups():
            r = random.random()
            g.officer_checked = r < Constants.checking_prob
            g.real_k = random.choice(Constants.K_CHOICES)


class Group(BaseGroup):
    real_k = models.FloatField()
    k_declare = models.FloatField(choices=Constants.K_CHOICES,
                                  widget=widgets.RadioSelectHorizontal)

    def k_declare_choices(self):
        return [i for i in Constants.K_CHOICES if i <= self.real_k]

    incentive = models.IntegerField()
    k_belief = models.FloatField()
    taxes_paid = models.CurrencyField()
    taxes_multiplied = models.CurrencyField()
    taxes_paid_back = models.CurrencyField()
    individual_share = models.CurrencyField()
    embezzled_amount = models.CurrencyField()
    fine_pool = models.IntegerField(initial=0)
    officer_checked = models.BooleanField()
    true_k = models.BooleanField()

    def set_payoffs(self):
        officer = self.get_player_by_role('officer')
        citizen = self.get_player_by_role('citizen')
        self.true_k = self.real_k == self.k_declare
        self.taxes_paid = sum([p.tax_paid for p in self.get_players()])
        self.taxes_multiplied = self.taxes_paid * self.real_k;
        self.taxes_paid_back = self.taxes_paid * self.k_declare;
        self.individual_share = self.taxes_paid_back / Constants.players_per_group

        self.embezzled_amount = self.taxes_multiplied - self.taxes_paid_back
        for p in self.get_players():
            p.payoff = p.endowment - p.tax_paid + self.individual_share

        if self.subsession.treatment != 'baseline':
            citizen.payoff -= self.incentive
            self.fine_pool += self.incentive

        officer.payoff += self.embezzled_amount

        officer.payoff += self.officer_checked * self.fine_pool * (self.true_k == self.subsession.sign)


class Player(BasePlayer):
    endowment = models.CurrencyField()
    tax_paid = models.CurrencyField()
    cq1_1, cq1_2, cq2_1, cq2_2, cq3_1, cq3_2 = [models.IntegerField() for _ in range(6)]

    def role(self):
        """defines that the first player in group will be a bureaucrat"""
        if self.id_in_group == 1:
            return 'officer'
        return 'citizen'
