from otree.api import Currency as c, currency_range, Submission
from .pages import *
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield Instructions,
        yield Examples,
        yield CQs, Constants.correct_answers
        yield BeforeTheGame,
        yield PayTax,
        if self.player.role() == 'officer':
            available_choices = self.group.k_declare_choices()
            yield Submission(KDeclare, dict(k_declare=random.choice(available_choices)), check_html=False)

        yield Results
        if self.player.role() == 'citizen':
            yield KBelief, dict(k_belief=random.choice(self.group.k_belief_choices()))
