from banksim.agent.bank import Bank
from banksim.agent.loan import Loan
from banksim.agent.saver import Saver


def update_car(schedule, car):
    for bank in [x for x in schedule.agents if isinstance(x, Bank)]:
        bank.upper_bound_cratio = 1.5 * car
