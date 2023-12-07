#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unboundedKnapsack(k, arr):
    # Write your code here
    print(k,arr)
    sums = set([0])
    for _ in range(k//min(arr)):
        sums2 = set(sums)
        for s in sums:
            for n in arr:
                sums2.add(s+n)
        sums = set(s for s in sums2 if s <= k)
        print(sums)
    ret = max(sums)
    print(ret)
    return ret
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()
