#!/usr/bin/env python
# encoding=utf8
N = int(input("Input int N: "))
if 0 <N < 100:
    w = len(bin(N)) - 2
    for i in range(1, N + 1):
        print('{0:{width}d} {0:{width}o}'
              '{0:{width}X} {0:{width}b}'.format(i, width=w))
else:
    print('N must between 1 and 99')
    exit(1)
