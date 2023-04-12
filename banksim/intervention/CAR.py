from banksim.agent.loan import Loan
from banksim.intervention.base import Intervention, InterventionInstance
import numpy as np


class CARIntervention(Intervention):
    def __init__(self, car_add_range=[0, 0.05, 0.1], bank_id_filter=None, step=235):
        self.bank_id_filter = bank_id_filter
        self.car_add_range = car_add_range
        self.step = step

    def get_instances(self):
        return [CARInterventionInstance(i, self.bank_id_filter, self.step) for i in self.car_add_range]


class CARInterventionInstance(InterventionInstance):
    def __init__(self, car_add, bank_id_filter=None, step=235):
        self.bank_id_filter = bank_id_filter
        self.car_add = car_add
        self.step = step

    def intervention(self, schedule, **kwargs):
        random_car_list = kwargs['random_car_list']
        random_car_list[self.step:] = [ round(i+self.car_add,4) for i in random_car_list[self.step:]]

    def id(self):
        return f'car{self.car_add}'
