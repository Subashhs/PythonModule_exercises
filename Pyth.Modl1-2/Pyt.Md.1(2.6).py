#Write a program that draws two random combinations of numbers for a combination lock:
#a 3-digit code where each number is between 0 and 9.
#a 4-digit code where each number is between 1 and 6..

import random

a = 0
b = 9
c = 3

draw = random.sample(range(a, b),c)
print(draw)

x = 1
y = 6
n = 4

new = random.sample(range(x, y),n)
print(new)