#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

from itertools import permutations

def isms(s):
    a,b,c,d,e,f,g,h,i = s
    return a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g

def formingMagicSquare(s):
    # Write your code here
    q = [z for z in permutations(range(1,9+1)) if isms(z)]
    return min(sum(abs(z[i] - s[i//3][i%3]) for i in range(9)) for z in q)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
