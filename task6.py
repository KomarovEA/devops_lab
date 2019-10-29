#!/usr/bin/env python
# encoding=utf8


def SplitStr(InputString):
    '''Split string to list of words'''
    return InputString.split(" ")


def ReversList(InputList):
    '''revers characters in InputList's words '''
    OutStr = ""
    for i in range(len(InputList) - 1):
        OutStr += (InputList[i][::-1])
        OutStr += " "
    OutStr += (InputList[len(InputList) - 1][::-1])
    return OutStr


if __name__ == "__main__":
    Str = input("Input string: ")
    Out = ReversList(SplitStr(Str))
    print(Out)
