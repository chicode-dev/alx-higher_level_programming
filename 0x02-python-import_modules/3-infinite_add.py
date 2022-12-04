#!/usr/bin/python3
from sys import argv
length = len(argv)
sum = 0
if length == 1:
    sum = 0
else:
    for num in range(1, length):
        number = argv[num]
        sum = sum + int(number)
print(f'{sum:d}')
