#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
on = number

if number < 0:
    sign = -1
else:
    sign = 1
number = abs(number)
ld = number % 10

if sign * ld > 5:
    print(f"Last digit of {on} is {sign * ld} and is greater than 5")
elif sign * ld == 0:
    print(f"Last digit of {on} is {sign * ld} and is zero")
elif sign * ld < 6 and ld != 0:
    print(f"Last digit of {on} is {sign * ld} and is less than 6 and not 0")
