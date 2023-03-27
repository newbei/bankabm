# coding: utf-8

import os
import sys
import time

p = '/mnt/nfsroot/hegang/code/ABM/CASES/bankabm'
if os.path.exists(p):
    sys.path.append(p)
    print('sys.path.append', p)
else:
    print('not append')

import itertools
import concurrent.futures

from banksim.logger import get_logger
from banksim.model import BankSim
from banksim.util.write_sqlitedb import init_database
from banksim.agent.bank import Bank

import random
import numpy as np

# To replicate the simulation result in this paper (ABBA: An Agent-Based Model of the Banking System - IMF)
#
#

logger = get_logger("scenario")


def exec_banksim_model(model_params):
    model = BankSim(**model_params)
    start = time.time()
    model.run_model(step_count=240)
    end = time.time()
    print('exec_banksim_model cost ', end - start,' secs')
    return True


def main(rep_count=1):
    init_database()
    for i in range(rep_count):

        logger.info(f'repcount : {i}')
        model_params = {"init_db": False,
                        "write_db": True,
                        "max_steps": 240,
                        "initial_saver": 10000,
                        "initial_bank": 10,
                        "initial_loan": 20000,
                        "initial_equity": 100,
                        "rfree": 0.01
                        }

        # lst_capital_req = [0.04, 0.08, 0.12, 0.16]
        lst_capital_req = [0.04, 0.08]
        # lst_reserve_ratio = [0.03, 0.045, 0.06]
        lst_reserve_ratio = [0.03]
        combination_car_res = list(itertools.product(lst_capital_req, lst_reserve_ratio))

        lst_model_params = list()
        for x in combination_car_res:
            model_params["car"] = x[0]
            model_params["min_reserves_ratio"] = x[1]
            model_params["random_state"] = i + 3000
            lst_model_params.append(model_params.copy())
        with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
            model_finish_cnt = 0
            for res in executor.map(exec_banksim_model, lst_model_params):
                if res:
                    model_finish_cnt = model_finish_cnt + 1
                    if model_finish_cnt % 10 == 0:
                        logger.info('Number of completed scenario: %3d', model_finish_cnt)
    logger.info('finished')


# Bank status
# for x in [x for x in model.schedule.agents if isinstance(x, Bank)]:
#     print("Bank{0:1d} - Reserve: {1:5.0f}, Equity: {2:5.0f}, Deposit: {3:5.0f}, Reserve_ratio: {4:5.3f}".
#           format(x.pos, x.bank_reserves, x.equity, x.bank_deposits, x.reserves_ratio))


if __name__ == "__main__":
    start = time.time()
    main(rep_count=1)
    end = time.time()
    print('total cost ', end - start, ' secs')
