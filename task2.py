#!/usr/bin/env python
# encoding=utf8
Str = input("Input string: ")
if Str == Str[::-1]:
    print("String", Str, "is palindrome")
else:
    print("It's not palindrome")
