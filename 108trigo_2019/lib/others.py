#!/usr/bin/python3

import sys
import math

from rest import *

def my_cos(tab):
    str = idy_maty(len(tab))
    i = 1
    while i < 40:
        if i % 2 == 0: str = my_add(str, my_div(my_cpow(tab, 2 * i),\
                                                my_facto(2 * i)))
        else: str = my_sub(str, my_div(my_cpow(tab, 2 * i), my_facto(2 * i)))
        i += 1
    return str

def my_sin(tab):
    str = tab
    i = 1
    while i < 40:
        if i % 2 == 0: str = my_add(str, my_div(my_cpow(tab, 2 * i + 1),\
                                                my_facto(2 * i + 1)))
        else: str = my_sub(str, my_div(my_cpow(tab, 2 * i + 1),\
                                       my_facto(2 * i + 1)))
        i += 1
    return str

def my_cosh(tab):
    str = idy_maty(len(tab))
    i = 1
    while i < 40:
        str = my_add(str, my_div(my_cpow(tab, 2 * i), my_facto(2 * i)))
        i += 1
    return str


def my_sinh(tab):
    str = tab
    i = 1
    while i < 40:
        str = my_add(str, my_div(my_cpow(tab, 2 * i + 1), my_facto(2 * i + 1)))
        i += 1
    return str

def my_exp(tab):
    str = idy_maty(len(tab))
    i = 1
    while i < 50:
        str = my_add(str, my_div(my_cpow(tab, i), my_facto(i)))
        i += 1
    return str
