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


class Subsession(BaseSubsession):
    treatment = models.StringField()

    def creating_session(self):
        self.treatment = self.session.config.get('treatment')


class Group(BaseGroup):
    k_declare = models.FloatField()
    incentive = models.IntegerField()
    k_belief = models.FloatField()

    def set_payoffs(self):
        print("SETTTING PAYOOFS")


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'individual'
        return 'state'
