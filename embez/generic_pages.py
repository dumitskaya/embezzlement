from otree.api import Currency as c, currency_range
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants


class Page(oTreePage):
    def extra_is_displayed(self):
        return True


class StatePage(Page):
    def is_displayed(self):
        return self.player.role() == 'state' and self.extra_is_displayed()


class IndividualPage(Page):
    def is_displayed(self):
        return self.player.role() == 'individual' and self.extra_is_displayed()
