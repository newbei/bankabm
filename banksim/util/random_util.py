import random


def random_car_list(car0, max_steps):
    cars = [car0]
    for i in range(max_steps + 10):
        if random.random() < 0.2:
            if random.random() > 0.5:
                cars.append(round(cars[-1] + 0.005, 3))
            else:
                cars.append(round(cars[-1] - 0.005, 3))
        else:
            cars.append(cars[-1])
    return cars


