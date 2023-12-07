#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairCut' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def fairCut(k, arr):
    # Write your code here
    n = len(arr)
    arr = sorted(arr)
    if k > n//2:
        k = n - k
    X = []
    Y = []
    i = 0
    j = 0
    arri = iter(arr)
    while i < k and j < n-k:
        a = next(arri)
        if k-1-2*i > n-k-1-2*j:
            X.append(a)
            i += 1
        else:
            Y.append(a)
            j += 1
    while i < k:
        X.append(next(arri))
        i += 1
    while j < n-k:
        Y.append(next(arri))
        j += 1
    return sum(abs(x-y) for x in X for y in Y)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = fairCut(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
