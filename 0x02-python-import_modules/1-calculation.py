#!/usr/bin/python3
import calculator_1 as cal
a = 10
b = 5
add = cal.add(a, b)
sub = cal.sub(a, b)
mul = cal.mul(a, b)
div = cal.div(a, b)
print(f'{a:d} + {b:d} = {add:d}')
print(f'{a:d} - {b:d} = {sub:d}')
print(f'{a:d} * {b:d} = {mul:d}')
print(f'{a:d} / {b:d} = {div:d}')
