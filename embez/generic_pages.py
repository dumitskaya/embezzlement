from otree.api import Currency as c, currency_range
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants


class Page(oTreePage):
    show_instructions = False
    def extra_is_displayed(self):
        return True

    def get_progress(self):
        totpages = self.participant._max_page_index
        curpage = self.participant._index_in_pages
        return f"{curpage / totpages * 100:.0f}"
class InstructionPage(Page):
    show_instructions = True

class OfficialPage(InstructionPage):
    def is_displayed(self):
        return self.player.role() == 'officer' and self.extra_is_displayed()


class CitizenPage(InstructionPage):
    def is_displayed(self):
        return self.player.role() == 'citizen' and self.extra_is_displayed()
