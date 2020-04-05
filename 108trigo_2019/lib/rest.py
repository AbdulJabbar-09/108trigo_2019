#!/usr/bin/python3

import sys
import math

from utils import *

def my_cpow(mat, n):
    str = mat
    i = 0
    while i < n - 1:
        str = my_mult(str, mat)
        i += 1
    return str

def my_div(mat, k):
    for i in range(len(mat)):
        j = 0
        while j < len(mat[0]):
            mat[i][j] /= k
            j += 1
    return mat

def usage():
    print("USAGE")
    print("    ./108trigo fun a0 a1 a2 ...\n")
    print("DESCRIPTION\n")
    print('    fun    function to be applied, among at least "EXP", "COS", \
"SIN", "COSH"')
    print('           and "SINH"\n')
    print("    ai     coeficients of the matrix")
    sys.exit(0)

def check_args():
    if "-h" in sys.argv: usage()
    if len(sys.argv) <= 2 or sys.argv[1] not in ["EXP", "COS", "SIN", "COSH",\
                                                 "SINH"]: sys.exit(84)
    try:
        for i in range(2, len(sys.argv)): sys.argv[i] = float(sys.argv[i])
    except ValueError: sys.exit(84)
