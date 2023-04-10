from banksim.intervention.base import Intervention, InterventionInstance
from banksim.agent.saver import Saver
import numpy as np


class F7WithdrawIntervention(Intervention):
    def __init__(self, withdraw_savers_range=range(0, 10), bank_id_filter=[1], step=239):
        self.bank_id_filter = bank_id_filter
        self.withdraw_savers_range = withdraw_savers_range
        self.step = step

    def get_instances(self):
        return [F7WithdrawInterventionInstance(i, self.bank_id_filter, self.step) for i in self.withdraw_savers_range]


class F7WithdrawInterventionInstance(InterventionInstance):
    def __init__(self, withdraw_savers, bank_id_filter=[1], step=239):
        self.bank_id_filter = bank_id_filter
        self.withdraw_savers = withdraw_savers
        self.step = step

    def intervention(self, schedule, **kwargs):
        bank = kwargs['bank']
        if self.step != schedule.steps:
            return
        # id_filter worked and bankid not in it
        if self.bank_id_filter is not None \
                and len(self.bank_id_filter) > 0 \
                and bank.unique_id not in self.bank_id_filter:
            return
        #
        savers = [x for x in schedule.agents if isinstance(x, Saver) and x.pos == bank.pos and
                  x.saver_solvent and x.owns_account]
        for saver in np.random.choice(savers, min(len(savers), self.withdraw_savers)):
            saver.bank_id = 9999
            saver.owns_account = False
            # TO DO: saver.saver_last_color = color
            # TO DO: change color Red
            bank.deposit_outflow = bank.deposit_outflow + saver.balance

    def id(self):
        return f'f7w{self.withdraw_savers}'
