import os
import time


class FileWriter(object):
    CACHE_SIZE = 100
    banks_cache = []

    def insert_agtbank_table_f2(self, simid, numstep, banks):
        # start = time.time()
        file_bank = f'result.{simid}.csv'
        created = os.path.exists(file_bank)
        with open(file_bank, 'a') as f:

            if not created:
                headers = '''AgtBankId,SimId,StepCnt,BankId,BankEquityT0,BankDepositT0,BankLoanT0,BankReserveT0,BankAssetT0,BankProvisionT0,BankRiskWgtAssetT0,BankEquityF2,BankLoanF2,BankReserveF2,BankAssetF2,BankProvisionF2,BankNetInterestIncomeF2,BankInterestIncomeF2,BankInterestExpenseF2,BankCapitalRatioF2,BankReservesRatioF2,BankRiskWgtAssetF2,BankDefaultedLoanF2,BankSolventF2,BankCapitalizedF2,BankCreditFailureF2,RiskWgtAmountDefaultedF2,BankLgdAmountF2,CAR,BankReserveF2_1\n'''
                f.write(headers)
            tmp_bank_f2s = [bank.bank_f2.get_all_variables() for bank in banks]
            strs = ''
            for tmp_bank_f2 in tmp_bank_f2s:
                tmp_bank_f2[0] = int(str(10000 + numstep) + str(10000 + tmp_bank_f2[3]))  # AgtBankId
                tmp_bank_f2[1] = simid
                tmp_bank_f2[2] = numstep
                strs = strs + ','.join([str(i) for i in tmp_bank_f2]) + '\n'
            f.write(strs)
        # print(time.time() - start, 's')
