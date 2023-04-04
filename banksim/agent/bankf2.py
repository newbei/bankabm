class BankF2(object):
    def __init__(self, bank_id):
        self.bank_id = bank_id

    def update_t0(self, bank):
        self.equity_t0 = bank.equity
        self.bank_deposits_t0 = bank.bank_deposits
        self.bank_loans_t0 = bank.bank_loans
        self.bank_reserves_t0 = bank.bank_reserves
        self.total_assets_t0 = bank.total_assets
        self.bank_provisions_t0 = bank.bank_provisions
        self.rwassets_t0 = bank.rwassets

    def update_f2(self, bank):
        self.equity_f2 = bank.equity
        self.bank_loans_f2 = bank.bank_loans
        self.bank_reserves_f2 = bank.bank_reserves
        self.total_assets_f2 = bank.total_assets
        self.bank_provisions_f2 = bank.bank_provisions

        self.net_interest_income_f2 = bank.net_interest_income
        self.interest_income_f2 = bank.interest_income
        self.interest_expense_f2 = bank.interest_expense

        self.capital_ratio_f2 = bank.capital_ratio
        self.reserves_ratio_f2 = bank.reserves_ratio
        self.rwassets_f2 = bank.rwassets

        self.defaulted_loans_f2 = bank.defaulted_loans
        self.bank_solvent_f2 = bank.bank_solvent
        self.bank_capitalized_f2 = bank.bank_capitalized
        self.credit_failure_f2 = bank.credit_failure

        # self.rw_wgt_defaulted_loans_f2 = 0 # update in code
        # self.car

    def clear(self):
        self.equity_t0 = 0
        self.bank_deposits_t0 = 0
        self.bank_loans_t0 = 0
        self.bank_reserves_t0 = 0
        self.total_assets_t0 = 0
        self.bank_provisions_t0 = 0
        self.rwassets_t0 = 0

        self.equity_f2 = 0
        self.bank_loans_f2 = 0
        self.bank_reserves_f2 = 0
        self.total_assets_f2 = 0
        self.bank_provisions_f2 = 0

        self.net_interest_income_f2 = 0
        self.interest_income_f2 = 0
        self.interest_expense_f2 = 0

        self.capital_ratio_f2 = 0
        self.reserves_ratio_f2 = 0
        self.rwassets_f2 = 0

        self.defaulted_loans_f2 = 0
        self.bank_solvent_f2 = 0
        self.bank_capitalized_f2 = False
        self.credit_failure_f2 = False

        self.rw_wgt_defaulted_loans_f2 = 0
        self.car = 0

    def get_all_variables(self):
        res = [
            '',  # AgtBankId
            '',  # SimId
            '',  # StepCnt
            self.bank_id,  # BankId
            self.equity_t0,
            self.bank_deposits_t0,
            self.bank_loans_t0,
            self.bank_reserves_t0,
            self.total_assets_t0,
            self.bank_provisions_t0,
            self.rwassets_t0,
            self.equity_f2,
            self.bank_loans_f2,
            self.bank_reserves_f2,
            self.total_assets_f2,
            self.bank_provisions_f2,
            self.net_interest_income_f2,
            self.interest_income_f2,
            self.interest_expense_f2,
            self.capital_ratio_f2,
            self.reserves_ratio_f2,
            self.rwassets_f2,
            self.defaulted_loans_f2,
            self.bank_solvent_f2,
            self.bank_capitalized_f2,
            self.credit_failure_f2,
            self.rw_wgt_defaulted_loans_f2,
            self.car
        ]
        return res