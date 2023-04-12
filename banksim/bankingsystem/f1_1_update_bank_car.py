from banksim.agent.bank import Bank
from banksim.agent.loan import Loan
from banksim.agent.saver import Saver


def update_car(schedule, car):
    for bank in [x for x in schedule.agents if isinstance(x, Bank)]:
        bank.upper_bound_cratio = 1.5 * car
        bank.car = car


def reset_before_step(schedule, car, mrr):
    for bank in [x for x in schedule.agents if isinstance(x, Bank)]:
        bank.approved_loans = 0
        bank.optimized_loans = 0
        bank.defaulted_loans = 0
        bank.deposit_inflow = 0
        bank.deposit_outflow = 0
        bank.net_deposit_flow = 0

        bank.upper_bound_cratio = 1.5 * car
        bank.car = car
        bank.mrr = mrr

        bank.bank_f2.clear()
        bank.bank_f2.update_t0(bank)
        bank.bank_f2.car = car
