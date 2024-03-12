#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
on = number

if number < 0:
    number *= -1

ld = number % 10

if ld > 5:
    print(f"Last digit of {on} is {number % 10} and is greater than 5")
elif ld == 0:
    print(f"Last digit of {on} is {number % 10} and is zero")
elif ld < 6 and ld != 0:
    print(f"Last digit of {on} is {number % 10} and is less than 6 and not 0")
