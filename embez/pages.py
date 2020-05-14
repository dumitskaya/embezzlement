from otree.api import Currency as c, currency_range
from ._builtin import WaitPage
from .generic_pages import Page, IndividualPage, StatePage
from .models import Constants


class Intro(Page):
    pass


class PayTax(Page):
    pass


class KDeclare(StatePage):
    form_model = 'group'
    form_fields = ['k_declare']


class Incentive(IndividualPage):
    form_model = 'group'
    form_fields = ['incentive']

    def extra_is_displayed(self):
        print("TREATMENT ", self.subsession.treatment)
        return self.subsession.treatment != 'baseline'


class KBelief(IndividualPage):
    form_model = 'group'
    form_fields = ['k_belief']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [
    Intro,
    PayTax,
    KDeclare,
    Incentive,
    KBelief,
    ResultsWaitPage,
    Results
]
