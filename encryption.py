#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    L = len(s)
    R = C = int(math.sqrt(L))
    if R * C < L:
        C += 1
    if R * C < L:
        R += 1
    assert R * C >= L
    words = []
    for m in range(C):
        words.append(''.join(s[n] for n in range(m,L,C)))
    return ' '.join(words)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
