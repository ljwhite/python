# Generate a list of 10 numbers, randomly between 10 and 15
# Map list to double values that are initially greater than 15
import random

accumulator = []

for i in range(10):
    i = random.randrange(1,50)
    accumulator.append(i)

print([x*x for x in accumulator if x >= 15])
