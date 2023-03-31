import os
import sqlite3
import zipfile
import configparser
from datetime import datetime, timezone


def insert_simulation_table(cursor, task):
    """
    Insert a row into Simulation table
    :param conn:
    :param task:
    :return:
    """

    sql = '''INSERT INTO Simulation(simid,title,simdate,randomstate,remark) VALUES(?,?,?,?,?)'''
    cursor.execute(sql, task)
    return cursor.lastrowid


def insert_agtbank_table(cursor, simid, numstep, banks):
    """

    :param cursor:
    :param banks:
    :return:
    """

    sql = '''INSERT INTO AgtBank(AgtBankId,SimId,StepCnt,BankId,BankEquity,BankDeposit,BankLoan,BankReserve,BankAsset,
    BankProvision,BankNProvision,BankDepositRate,BankIbCredit,BankIbDebit,BankNetInterestIncome,BankInterestIncome,
    BankInterestExpense,BankIbInterestIncome,BankIbInterestExpense,BankIbNetInterestIncome,BankIbCreditLoss,
    BankRiskWgtAsset,BankDividend,BankCumDividend,BankDepositOutflow,BankDepositInflow,BankNetDepositflow,
    BankDefaultedLoan,BankSolvent,BankCapitalized,BankCreditFailure,BankLiquidityFailure,BankStepDate,BankDepositOptimize,
    BankOptimizedLoan,BankApprovedLoan) VALUES(
    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    col_date = datetime.now(timezone.utc)

    tmp_banks = [bank.get_all_variables() for bank in banks]
    for tmp_bank in tmp_banks:
        tmp_bank[0] = int(str(10000 + numstep) + str(10000 + tmp_bank[3]))  # AgtBankId
        tmp_bank[1] = simid
        tmp_bank[2] = numstep
        tmp_bank[32] = col_date
    # for bank in banks:
    #     bank_vars = bank.get_all_variables()
    #     bank_vars[0] = int(str(10000 + numstep) + str(10000 + bank_vars[3]))  # AgtBankId
    #     bank_vars[1] = simid
    #     bank_vars[2] = numstep
    #     bank_vars[32] = col_date
    #     # cursor.execute(sql, tuple(bank_vars))
    cursor.executemany(sql, tmp_banks)

    return cursor.lastrowid


def insert_agtsaver_table(cursor, simid, numstep, savers):
    """

    :param cursor:
    :param simid:
    :param numstep:
    :param savers:
    :return:
    """
    sql = '''INSERT INTO AgtSaver(AgtSaverId,SimId,StepCnt,SaverId,SaverBalance,SaverWithdrawProb,SaverExitProb,SaverBankId,
    SaverRegionId,SaverOwnAccount,SaverSolvent,SaverExit,SaverCurrent,SaverStepDate) Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

    col_date = datetime.now(timezone.utc)
    tmp_savers = [saver.get_all_variables() for saver in savers]
    for tmp_saver in tmp_savers:
        tmp_saver[0] = int(str(10000 + numstep) + str(10000 + tmp_saver[3]))  # AgtSaverId
        tmp_saver[1] = simid
        tmp_saver[2] = numstep
        tmp_saver[13] = col_date
    cursor.executemany(sql, tmp_savers)

    return cursor.lastrowid


def insert_agtloan_table(cursor, simid, numstep, loans):
    """

    :param cursor:
    :param simid:
    :param numstep:
    :param loans:
    :return:
    """

    sql = '''INSERT INTO AgtLoan(AgtLoanId,SimId,StepCnt,LoanId,LoanProbDefault,LoanAmount,LoanRiskWgt,LoanRiskWgtAmt,
    LoanLgdAmt,LoanRecovery,LoanRcvryRate,LoanFireSaleLoss,LoanRating,LoanRateQuote,LoanRateReservation,LoanPlusRate,
    LoanInterestPymt,LoanRegionId,LoanApproved,LoanSolvent,LoanDumped,LoanLiquidated,LoanBankId,LoanStepDate) 
    Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

    col_date = datetime.now(timezone.utc)
    tmp_loans = [loan.get_all_variables() for loan in loans]
    for tmp_loan in tmp_loans:
        tmp_loan[0] = int(str(10000 + numstep) + str(10000 + tmp_loan[3]))  # AgtloanId
        tmp_loan[1] = simid
        tmp_loan[2] = numstep
        tmp_loan[-1] = col_date
    cursor.executemany(sql, tmp_loans)

    return cursor.lastrowid


def insert_agtibloan_table(cursor, simid, numstep, ibloans):
    """

    :param cursor:
    :param simid:
    :param numstep:
    :param ibloans:
    :return:
    """

    sql = '''INSERT INTO AgtIbLoan(AgtIbLoanId,SimId,StepCnt,IbLoanId,IbLoanRate,IbLoanAmount,IbLoanCreditor,
    IbLoanDebtor,IbLoanStepDate) Values(?,?,?,?,?,?,?,?,?)'''

    col_date = datetime.now(timezone.utc)
    tmp_loans = [loan.get_all_variables() for loan in ibloans]
    for tmp_loan in tmp_loans:
        tmp_loan[0] = int(str(10000 + numstep) + str(10000 + tmp_loan[3]))  # AgtloanId
        tmp_loan[1] = simid
        tmp_loan[2] = numstep
        tmp_loan[-1] = col_date
    cursor.executemany(sql, tmp_loans)

    return cursor.lastrowid


def init_database():
    config = configparser.ConfigParser()
    config.read('conf/config.ini')
    sqlite_db = config['SQLITEDB']['file']
    db_init_query = config['SQLITEDB']['init_query']
    if os.path.isfile(sqlite_db):
        compression = zipfile.ZIP_DEFLATED
        with zipfile.ZipFile(sqlite_db + datetime.now().strftime('%Y%m%d%H%M') + '.zip', 'w') as zf:
            try:
                zf.write(sqlite_db, compress_type=compression)
            except:
                raise Exception("SQLITE DB file compression error")
            finally:
                zf.close()
    try:
        conn = sqlite3.connect(sqlite_db)
        db_cursor = conn.cursor()
        fin = open(db_init_query, 'r')
        db_cursor.executescript(fin.read())
        conn.commit()
    except:
        raise Exception("SQLite DB init error")
    finally:
        db_cursor.close()
        conn.execute("VACUUM")
        conn.close()
