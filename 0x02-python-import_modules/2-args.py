#!/usr/bin/python3
from sys import argv
totalarguments = len(argv)
count = 1
if totalarguments == 1:
    print(f'0 arguments.')
elif totalarguments == 2:
    argument = argv[1]
    print(f'1 argument:')
    print(f'{count:d}: {argument:s}')
else:
    print(f'{totalarguments-1:d} arguments:')
    for num in range(2, totalarguments+1):
        argument = argv[count]
        count += 1
        print(f'{count-1:d}: {argument:s}')
