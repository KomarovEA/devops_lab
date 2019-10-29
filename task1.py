#!/usr/bin/env python
# encoding=utf8
N: int = int(input("Input int N: "))
if 0 < N < 21:
    i = 1
    while i < N:
        print(i, '^2 is:', i * i)
        i += 1
else:
    print("N must between 1 and 20")
    exit(1)

