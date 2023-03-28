import random


def random_car_list(car0, max_steps, add_car):
    cars = [car0]
    for i in range(max_steps + 10):
        if random.random() < 0.2:
            if random.random() > 0.5:
                cars.append(round(cars[-1] + 0.005, 3))
            else:
                cars.append(round(cars[-1] - 0.005, 3))
        else:
            cars.append(cars[-1])

        if i == max_steps - 4:
            cars[-1] = round(cars[-1] + add_car, 3)
    return cars

def random_mrr_list(mrr0, max_steps, add_car):
    mrr_min = 0.005
    mrr_max = 0.1
    mrrs = [mrr0]
    for i in range(max_steps + 10):
        if random.random() < 0.2:
            if random.random() > 0.5 or mrrs[-1] <= mrr_min:
                mrrs.append(round(mrrs[-1] + 0.005, 3))
            else:
                mrrs.append(round(mrrs[-1] - 0.005, 3))
        else:
            mrrs.append(mrrs[-1])

        if i == max_steps - 24:
            mrrs[-1] = round(mrrs[-1] + add_car, 3)
    return mrrs
