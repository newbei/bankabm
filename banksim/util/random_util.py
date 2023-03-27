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
