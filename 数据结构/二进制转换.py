#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/6/11 23:35

from  pythonds.basic import Stack


def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


n = 8
print(divideBy2(n))