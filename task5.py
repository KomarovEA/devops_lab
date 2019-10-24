#!/usr/bin/env python
# encoding=utf8
n, m = list(map(int, input().split()))
ns = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
res = 0
for x in ns:
    if x in A:
        res += 1
    elif x in B:
        res -= 1
print(res)
