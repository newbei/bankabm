from banksim.agent.loan import Loan
from banksim.intervention.base import Intervention, InterventionInstance
from banksim.agent.saver import Saver
import numpy as np


class F2DepositIntervention(Intervention):
    def __init__(self, deposit_change_range=range(0, 10), bank_id_filter=[1], step=239):
        self.bank_id_filter = bank_id_filter
        self.deposit_change_range = deposit_change_range
        self.step = step

    def get_instances(self):
        return [F2DepositInterventionInstance(i, self.bank_id_filter, self.step) for i in self.deposit_change_range]


class F2DepositInterventionInstance(InterventionInstance):
    def __init__(self, deposit_change, bank_id_filter=[1], step=239):
        self.bank_id_filter = bank_id_filter
        self.deposit_change = deposit_change
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
        savers = [x for x in schedule.agents if isinstance(x, Saver) and x.pos == bank.pos and
                  x.saver_solvent and x.owns_account]
        for saver in np.random.choice(savers, min(len(savers), self.deposit_change)):
            saver.bank_id = 9999
            saver.owns_account = False
            # TO DO: saver.saver_last_color = color
            # TO DO: change color Red
            bank.deposit_outflow = bank.deposit_outflow + saver.balance
            bank.bank_deposits = bank.bank_deposits - 1
            bank.bank_f2.bank_deposits_t0 = bank.bank_deposits

    def id(self):
        return f'f2d{self.deposit_change}'
