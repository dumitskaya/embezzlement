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
    pass
class BeforeTheGame(InstructionPage):
    pass


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
    PayTax,
    KDeclare,
    Incentive,
    KBelief,
    ResultsWaitPage,
    Results
]
