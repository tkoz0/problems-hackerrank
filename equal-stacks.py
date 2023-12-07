#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    h1,h2,h3 = h1[::-1],h2[::-1],h3[::-1]
    a1,a2,a3 = sum(h1),sum(h2),sum(h3)
    while a1 != a2 or a2 != a3:
        m = max(a1,a2,a3)
        if m == 0:
            break
        if a1 == m:
            a1 -= h1.pop()
        if a2 == m:
            a2 -= h2.pop()
        if a3 == m:
            a3 -= h3.pop()
    return a1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
