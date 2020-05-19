from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Start(Page):
    def is_displayed(self):
        return self.round_number == 1


class SQ1(Page):
    def is_displayed(self):
        return self.round_number == 1


class SQ2(Page):
    def is_displayed(self):
        return self.round_number == 1


class SQ3(Page):
    def is_displayed(self):
        return self.round_number == 1


class SQ4(Page):
    def is_displayed(self):
        return self.round_number == 1


class SQ5(Page):
    def is_displayed(self):
        return self.round_number == 1


class Roles(Page):
    pass


class Officer(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = 'player'
    form_fields = ['set_k']


class Wait(WaitPage):
    after_all_players_arrive = 'do_all'


class Results(Page):
    form_model = 'player'
    form_fields = ['guess']


class Wait2(WaitPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    wait_for_all_groups = True


class Final(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class Survey(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = ['gender', 'education', 'age', 'marital_status', 'religion', 'relative_position_in_region',
                   'similar_care_society', 'similar_care_nearby', 'justified_subsidies', 'justified_freeride',
                   'justified_theft', 'justified_tax_evasion', 'justified_corruption', 'justified_violence',
                   'fairness_general', 'positive_reciprocity', 'negative_reciprocity', 'abuse_you', 'honest_Russia',
                   'party_Russia', 'income']


class OfficerQ(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 1

    form_model = 'player'
    form_fields = ['q1', 'q2']


class CitizenQ(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group != 1

    form_model = 'player'
    form_fields = ['q3', 'q4']


class Code(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [SQ1, SQ2, SQ3, SQ4, SQ5,
                 Roles, Officer, Wait, Results, Wait2, Final,
                 OfficerQ, CitizenQ, Survey, Code]
