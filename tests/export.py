import pandas as pd
import sqlite3

cols = 'AgtBankId, SimId, StepCnt, BankId, BankEquity, BankDeposit, BankLoan, BankReserve, BankAsset, BankProvision, BankNProvision, BankDepositRate, BankIbCredit, BankIbDebit, BankNetInterestIncome, BankInterestIncome, BankInterestExpense, BankIbInterestIncome, BankIbInterestExpense, BankIbNetInterestIncome, BankIbCreditLoss, BankRiskWgtAsset, BankDividend, BankCumDividend, BankDepositOutflow, BankDepositInflow, BankNetDepositflow, BankDefaultedLoan, BankSolvent, BankCapitalized, BankCreditFailure, BankLiquidityFailure, BankStepDate'
cols = cols.replace(' ', '').split(',')
print(cols)


def get_data(file_path):
    mydb = sqlite3.connect(file_path)

    cursor = mydb.cursor()
    cursor.execute(
        "SELECT AgtBankId, SimId, StepCnt, BankId, BankEquity, BankDeposit, BankLoan, BankReserve, BankAsset, BankProvision, BankNProvision, BankDepositRate, BankIbCredit, BankIbDebit, BankNetInterestIncome, BankInterestIncome, BankInterestExpense, BankIbInterestIncome, BankIbInterestExpense, BankIbNetInterestIncome, BankIbCreditLoss, BankRiskWgtAsset, BankDividend, BankCumDividend, BankDepositOutflow, BankDepositInflow, BankNetDepositflow, BankDefaultedLoan, BankSolvent, BankCapitalized, BankCreditFailure, BankLiquidityFailure, BankStepDate FROM AgtBank;")
    tables = cursor.fetchall()
    data = pd.DataFrame(tables, columns=cols)
    cursor.execute("SELECT remark from Simulation;")
    mrrs = cursor.fetchall()
    mrrs_arr = mrrs[0][0].replace('[', '').replace(']', '').replace(' ', '').split(',')
    data['MRR'] = data['StepCnt'].map(lambda x: mrrs_arr[x])
    return data


def data_processing(df, bank_id):
    # 筛选bankidId=bank_id的银行
    df_bank2 = df[df['BankId'] == bank_id]
    df_bank2 = df_bank2.reset_index(drop=True)

    # # bankidId=2的银行  Shift 1
    df_bank2_s1 = df_bank2.shift(1)
    df_bank2_s1 = df_bank2_s1.reset_index(drop=True)

    # # bankidId=2的银行 shift 数据作为 T0

    df_bank2_s1_0 = df_bank2_s1[
        ['BankEquity', 'BankReserve', 'BankCapitalized', 'BankSolvent', 'BankDeposit', 'BankLoan', 'BankIbCredit']]
    df_bank2_s1_0.columns = ['BankEquity_0', 'BankReserve_0', 'BankCapitalized_0', 'BankSolvent_0', 'BankDeposit_0',
                             'BankLoan_0', 'BankIbCredit_0']
    df_bank2_s1_0 = df_bank2_s1_0.reset_index(drop=True)

    # # 计算Loan变化
    LoanChange = df_bank2['BankLoan'] - df_bank2_s1['BankLoan']

    # # 计算Saver变化
    BankNetDepositflow = df_bank2['BankDeposit'] - df_bank2_s1['BankDeposit']

    # # 数据集合并
    df_bank2_merge = df_bank2.copy()

    df_bank2_merge = pd.concat([df_bank2_merge, df_bank2_s1_0], 1)
    df_bank2_merge['BankNetDepositflow'] = BankNetDepositflow
    df_bank2_merge['BankLoanChange'] = LoanChange
    return df_bank2_merge[1:]


result_files = [r'D:\datas\abm\results_v0.0.2_4\result.sqlite',
                r'D:\datas\abm\results_v0.0.2_4\result.sqlite202303291424\result.sqlite',
                r'D:\datas\abm\results_v0.0.2_4\result.sqlite202303291431\result.sqlite',
                ]

print('begin')
for i in range(len(result_files)):
    data = get_data(result_files[i])

    cols_drop = ['AgtBankId', 'SimId', 'BankNProvision', 'BankDepositRate', 'BankCumDividend', 'BankDepositOutflow',
                 'BankDepositInflow', 'BankStepDate', 'BankDefaultedLoan', 'BankIbCreditLoss', 'BankLiquidityFailure']
    df = data.drop(cols_drop, 1)

    df_new = pd.DataFrame()
    for i in range(10):
        df_new = pd.concat([df_new, data_processing(df, i + 1)], 0)
    print(df_new.shape)

    mrr_last = data['MRR'][-2:-1].values[0]
    df_new.to_csv(f'data_{mrr_last}.csv', index=False)
    print(mrr_last)
#     print(f'saved data{i}.csv')
print('end')
