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

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'embez'
    players_per_group = None
    num_rounds = 1
    k_min = 1
    k_max = 3
    individial_endowment = 10
    tax_rate = .5
    coef = .2


class Subsession(BaseSubsession):
    treatment = models.StringField()

    def creating_session(self):
        self.treatment = self.session.config.get('treatment')


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

    def set_payoffs(self):
        self.taxes_paid = sum([p.tax_paid for p in self.get_players()])
        self.taxes_multiplied = self.taxes_paid * self.real_k;
        self.self.taxes_paid_back = self.taxes_paid * self.k_declare;
        self.individual_share = self.taxes_paid_back / Constants.players_per_group
        state = self.get_player_by_role('state')
        self.embezzled_amount = self.taxes_multiplied - self.taxes_paid_back
        for p in self.get_players():
            p.payoff = p.endowment - p.tax_paid + self.individual_share
        state.payoff += self.embezzled_amount


class Player(BasePlayer):
    endowment = models.CurrencyField()
    tax_paid = models.CurrencyField()

    def role(self):
        if self.id_in_group == 1:
            return 'individual'
        return 'state'
