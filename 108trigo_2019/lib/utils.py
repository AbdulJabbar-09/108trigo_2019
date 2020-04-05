#!/usr/bin/python3

import sys
import math

def idy_maty(n):
    str = []
    for i in range(n):
        tab = []
        for j in range(n):
            tab.append(1 if j == i else 0)
        str.append(tab)
    return str

def my_facto(a):
    i = 1
    k = 1
    while k < a + 1:
        i *= k
        k += 1
    return i

def my_mult(ma_one, ma_two):
    str = []
    for i in range(len(ma_one)):
        tab = []
        for j in range(len(ma_two[0])):
            a = 0
            for k in range(len(ma_one[0])):
                a += ma_one[i][k] * ma_two[k][j]
            tab.append(a)
        str.append(tab)
    return str

def my_add(ma_one, ma_two):
    str = []
    for i in range(len(ma_one)):
        c = []
        for j in range(len(ma_one[0])):
            c.append(ma_one[i][j] + ma_two[i][j])
        str.append(c)
    return str

def my_sub(ma_one, ma_two):
    str = []
    for i in range(len(ma_one)):
        c = []
        for j in range(len(ma_one[0])):
            c.append(ma_one[i][j] - ma_two[i][j])
        str.append(c)
    return str
