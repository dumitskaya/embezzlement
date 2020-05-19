from otree.api import Currency as c, currency_range
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants


class Page(oTreePage):
    def extra_is_displayed(self):
        return True


class OfficialPage(Page):
    def is_displayed(self):
        return self.player.role() == 'officer' and self.extra_is_displayed()


class CitizenPage(Page):
    def is_displayed(self):
        return self.player.role() == 'citizen' and self.extra_is_displayed()
