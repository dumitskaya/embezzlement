from otree.api import Currency as c, currency_range
from ._builtin import WaitPage
from .generic_pages import Page, OfficialPage, CitizenPage, InstructionPage
from .models import Constants


class FirstWP(WaitPage):
    group_by_arrival_time = True
    after_all_players_arrive = 'after_group_is_formed'


class Instructions(InstructionPage):
    pass


class Examples(InstructionPage):
    pass


class CQs(InstructionPage):
    form_model = 'player'
    form_fields = [
        "cq1_1",
        "cq1_2",
        "cq2_1",
        "cq2_2",
        "cq3_1",
        "cq3_2",
    ]


class BeforeTheGame(InstructionPage):
    def vars_for_template(self):
        qs = Constants.correct_answers
        results = [getattr(self.player, k) == v for k, v in qs.items()]

        return dict(results=results)


class PayTax(InstructionPage):
    def before_next_page(self):
        self.player.tax_paid = self.player.endowment * Constants.tax_rate


class KDeclare(OfficialPage):
    form_model = 'group'
    form_fields = ['k_declare']


class KBelief(CitizenPage):
    form_model = 'group'
    form_fields = ['k_belief']

    def before_next_page(self):
        self.player.set_guess_payoff()


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass

class Incentives_Off(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1
    template_name = 'questionnaire/Incentives_Off.html'
    form_model = 'player'
    form_fields = [
            'off_pos',
            'off_neg'
    ]

class Incentives_Cit(Page):
    def is_displayed(self):
        return self.player.id_in_group != 1
    template_name = 'questionnaire/Incentives_Cit.html'
    form_model = 'player'
    form_fields = [
            'cit_pos',
            'cit_neg'
    ]
class Questions(Page):
    template_name = 'questionnaire/Questions.html'
    form_model = 'player'
    form_fields = [
            'quest'
    ]
page_sequence = [
    FirstWP,
    Instructions,
    Examples,
    CQs,
    BeforeTheGame,
    PayTax,
    KDeclare,
    ResultsWaitPage,
    Results,
    KBelief,
    Incentives_Off,
    Incentives_Cit,
    Questions,
]
