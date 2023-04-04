from banksim.agent.loan import Loan
from banksim.intervention.base import Intervention, InterventionInstance
import numpy as np


class F2LoanIntervention(Intervention):
    def __init__(self, default_loans_range=range(0, 10), bank_id_filter=[1], step=239):
        self.bank_id_filter = bank_id_filter
        self.default_loans_range = default_loans_range
        self.step = step

    def get_instances(self):
        return [F2LoanInterventionInstance(i, self.bank_id_filter, self.step) for i in self.default_loans_range]


class F2LoanInterventionInstance(InterventionInstance):
    def __init__(self, default_loans, bank_id_filter=[1], step=239):
        self.bank_id_filter = bank_id_filter
        self.default_loans = default_loans
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

        loans_with_bank = [x for x in schedule.agents if isinstance(x, Loan) and x.pos == bank.pos and
                           x.loan_approved and x.loan_solvent]
        for loan in np.random.choice(loans_with_bank, min(len(loans_with_bank), self.default_loans)):
            loan.loan_solvent = False
            loan.rwamount = loan.rweight * loan.amount
