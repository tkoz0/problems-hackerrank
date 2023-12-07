#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    af = dict()
    bf = dict()
    for a in arr:
        if a not in af:
            af[a] = 0
        af[a] += 1
    for b in brr:
        if b not in bf:
            bf[b] = 0
        bf[b] += 1
    ret = []
    for n in bf.keys():
        if n not in af or af[n] != bf[n]:
            ret.append(n)
    return sorted(ret)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
