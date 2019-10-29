#!/usr/bin/env python
# encoding=utf8
w, h = list(map(int, input('Input canvas size (w h): ').split()))
n = int(input('Input number of rectangles (n): '))
if (1 <= w <= 100) and (1 <= h <= 100) and (0 <= n <= 5000):
    a = [0] * (h)
    for i in range(0, w-1):
        a[i] = [0] * (h)
    for i in range(1, n + 1):
        x1, y1, x2, y2 = list(map(int, input(
            'Input the coordinates of the upper left and lowerright'
            'corners of the rectangle, respectively (x1, y1, x2, y2): ').split()))
        for y in range(y1+1, y2):
            for x in range(x1+1, x2):
                a[y][x] = 1
    c = 0
    for y in range(0, h-1):
        for x in range(0, w-1):
            c += 1 - a[y][x]
    print("unfinished canvas area is ", c)
else:
    exit('Illegal input: w and h must between 1 and 100,'
         'n must between 0 and 5000')
