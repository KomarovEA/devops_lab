#!/usr/bin/env python
# encoding=utf8
w, h = list(map(int, input("Input canvas size (w h): ").split()))
n = int(input("Input number of rectangles (n): "))
if (w < 1) | (w > 100) | (h < 1) | (h > 100) | (n < 0) | (n > 5000):
    exit("Illegal input: w and h must between 1 and 100,\
     n must between 0 and 5000")
a = [0] * 100
for i in range(100):
    a[i] = [0] * 100
for i in range(n):
    x1, y1, x2, y2 = list(map(int, input(
        "Input the coordinates of the upper left and lowerright\
         corners of the rectangle, respectively (x1, y1, x2, y2): ").split()))
    for y in range(y1, y2):
        for x in range(x1, x2):
            a[x - 1][y - 1] = 1
c = 0
for y in range(1, h):
    for x in range(1, w):
        c = c + 1 - a[x - 1][y - 1]
print("unfinished canvas area is ", c)
