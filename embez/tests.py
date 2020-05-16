from otree.api import Currency as c, currency_range
from .pages import *
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield Intro
        yield PayTax,
        if self.player.role() == 'state':
            yield KDeclare, dict(k_declare=random.uniform(Constants.k_min, self.group.real_k))
        else:
            if self.subsession.treatment != 'baseline':
                yield Incentive, dict(incentive=random.randrange(0, self.player.endowment))
            yield KBelief, dict(k_belief=random.uniform(Constants.k_min, Constants.k_max))
        yield Results
