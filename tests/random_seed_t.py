import random
import time
import os


class Foo():
    def __init__(self, random_state):
        self.random_state = random_state
        random.seed(self.random_state)

    def gen(self):
        print(self.random_state, random.randint(1, 10))


f1 = Foo(1)
f2 = Foo(1)

# for i in range(10):
#     f1.gen()
#     f2.gen()

start = time.time()
time.sleep(2)
end = time.time()
print(end - start)

# for i in range(10):
#     random.seed(5)
#     print(random.randint(1, 10))
