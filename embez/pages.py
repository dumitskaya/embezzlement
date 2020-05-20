from otree.api import Currency as c, currency_range
from ._builtin import WaitPage
from .generic_pages import Page, OfficialPage, CitizenPage, InstructionPage
from .models import Constants


class Intro(Page):
    pass


class Instructions(InstructionPage):
    pass


class Examples(InstructionPage):
    pass


class CQs(InstructionPage):
    form_model = 'player'
    form_fields = ["cq1_1", "cq1_2", "cq2_1", "cq2_2", "cq3_1", "cq3_2", ]


class BeforeTheGame(InstructionPage):
    def vars_for_template(self):
        qs = Constants.correct_answers
        results = [getattr(self.player, k) == v for k, v in qs.items()]
        return results


class PayTax(InstructionPage):
    def before_next_page(self):
        self.player.tax_paid = self.player.endowment * Constants.tax_rate


class KDeclare(OfficialPage):
    form_model = 'group'
    form_fields = ['k_declare']


class Incentive(CitizenPage):
    form_model = 'group'
    form_fields = ['incentive']

    def extra_is_displayed(self):
        print("TREATMENT ", self.subsession.treatment)
        return self.subsession.treatment != 'baseline'


class KBelief(CitizenPage):
    form_model = 'group'
    form_fields = ['k_belief']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [
    Intro,
    Instructions,
    Examples,
    CQs,
    BeforeTheGame,
    # PayTax,
    # KDeclare,
    # Incentive,
    # KBelief,
    # ResultsWaitPage,
    # Results
]
