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
    individual_endowment = 10
    tax_rate = .5
    coef = .2
    checking_prob = .3


class Subsession(BaseSubsession):
    treatment = models.StringField()
    sign = models.BooleanField(initial=True)

    def creating_session(self):
        self.treatment = self.session.config.get('treatment')
        if self.treatment == 'negative':
            self.sign = False
        for p in self.get_players():
            p.endowment = Constants.individual_endowment
        for g in self.get_groups():
            r = random.random()
            g.state_checked = r < Constants.checking_prob
            g.real_k = random.uniform(Constants.k_min, Constants.k_max)


class Group(BaseGroup):
    real_k = models.FloatField()
    k_declare = models.FloatField()
    incentive = models.IntegerField()
    k_belief = models.FloatField()
    taxes_paid = models.CurrencyField()
    taxes_multiplied = models.CurrencyField()
    taxes_paid_back = models.CurrencyField()
    individual_share = models.CurrencyField()
    embezzled_amount = models.CurrencyField()
    fine_pool = models.IntegerField(initial=0)
    state_checked = models.BooleanField()
    true_k = models.BooleanField()

    def set_payoffs(self):
        state = self.get_player_by_role('state')
        individual = self.get_player_by_role('individual')
        self.true_k = self.real_k == self.k_declare
        self.taxes_paid = sum([p.tax_paid for p in self.get_players()])
        self.taxes_multiplied = self.taxes_paid * self.real_k;
        self.taxes_paid_back = self.taxes_paid * self.k_declare;
        self.individual_share = self.taxes_paid_back / Constants.players_per_group

        self.embezzled_amount = self.taxes_multiplied - self.taxes_paid_back
        for p in self.get_players():
            p.payoff = p.endowment - p.tax_paid + self.individual_share

        if self.subsession.treatment != 'baseline':
            individual.payoff -= self.incentive
            self.fine_pool += self.incentive

        state.payoff += self.embezzled_amount

        state.payoff += self.state_checked * self.fine_pool * (self.true_k == self.subsession.sign)


class Player(BasePlayer):
    endowment = models.CurrencyField()
    tax_paid = models.CurrencyField()

    def role(self):
        if self.id_in_group == 1:
            return 'individual'
        return 'state'
