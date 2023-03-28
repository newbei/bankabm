import random
from banksim.util.random_util import random_car_list,random_mrr_list

def test_random_car_list():

    random.seed(3001)
    print(random_car_list(0.08, 240, 0)[236:])

    random.seed(3001)
    print(random_car_list(0.08, 240, 0.005)[236:])

    random.seed(3001)
    print(random_car_list(0.08, 240, 0.01)[236:])

def test_random_mrr_list():

    random.seed(3001)
    print(random_mrr_list(0.03, 240, 0)[236:])

    random.seed(3001)
    print(random_mrr_list(0.03, 240, 0.005)[236:])

    random.seed(3001)
    print(random_mrr_list(0.03, 240, 0.01)[236:])