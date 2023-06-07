#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    r = ((-1 * number) % 10) * (-1)
else:
    r = number % 10
if r < 0:
    print(f"Last digit of {number} is {r} and is less than 6 and not 0")
elif r == 0:
    print(f"Last digit of {number} is {r} and is 0")
elif r > 5:
    print(f"Last digit of {number} is {r} and is greater than 5")
