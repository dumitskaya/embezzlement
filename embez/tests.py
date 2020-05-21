from otree.api import Currency as c, currency_range
from .pages import *
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield Intro,
        yield Instructions,
        yield Examples,
        yield CQs, Constants.correct_answers
        yield BeforeTheGame,
        yield PayTax,
        if self.player.role() == 'officer':
            available_choices = self.group.k_declare_choices()
            yield KDeclare, dict(k_declare=random.choice(available_choices))
        else:
            if self.subsession.treatment != 'baseline':
                yield Incentive, dict(incentive=random.randrange(0, self.player.endowment))

        yield Results
        if self.player.role() == 'citizen':
            yield KBelief, dict(k_belief=random.choice(Constants.K_CHOICES))
