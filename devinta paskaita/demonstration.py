from random import sample

numbers = sample(range(1, 10001), 5)

numbers_false = [100,23213,214124,12421]
numbers_false[0], numbers_false[1] = numbers_false[1], numbers_false[0]

