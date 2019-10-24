#!/usr/bin/env python
# encoding=utf8
from typing import List

Str = input("Input string: ")
Lst: List[str] = Str.split(" ")
Out: str = ""
i: str
for i in range(len(Lst) - 1):
    Out += (Lst[i][::-1])
    Out += " "
Out += (Lst[len(Lst) - 1][::-1])
print(Out)
