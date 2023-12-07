#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestIncreasingSubsequence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestIncreasingSubsequence(arr):
    # Write your code here
    n = len(arr)
    a = [arr[0]]
    for i in range(1,n):
        if arr[i] > a[-1]:
            a.append(arr[i])
        else:
            lo,hi = 0,len(a)-1
            while lo<hi:
                m = (lo+hi)//2
                if a[m] < arr[i]:
                    lo = m+1
                else:
                    hi = m
            a[lo] = arr[i]
    return len(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
