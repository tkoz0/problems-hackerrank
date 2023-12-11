#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    freq = dict()
    for a in arr:
        if a not in freq:
            freq[a] = 0
        freq[a] += 1
    ba,bf = next(iter(freq.items()))
    for a,f in freq.items():
        if f > bf or (f == bf and a < ba):
            ba,bf = a,f
    return ba

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
