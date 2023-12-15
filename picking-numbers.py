#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    freq = dict()
    for z in a:
        if z not in freq:
            freq[z] = 0
        freq[z] += 1
    ret = max(freq.values())
    keys = sorted(freq.keys())
    for i in range(1,len(keys)):
        if (keys[i]-keys[i-1]) in [-1,1]:
            ret = max(ret,freq[keys[i]]+freq[keys[i-1]])
    return ret
    ''' contiguous subarray (misinterpretation)
    n = len(a)
    i,j = 0,0
    while j+1 < n and a[j+1] == a[i]:
        j += 1
    ret1 = j-i+1
    ret2 = 0
    while j+1 < n:
        i2,j2 = j+1,j+2
        while j2+1 < n and a[j2+1] == a[i2]:
            j2 += 1
        ret1 = max(ret1,j2-i2+1)
        if (a[i]-a[i2]) in [-1,1]:
            ret2 = max(ret2,j2-i+1)
        i,j = i2,j2
    return max(ret1,ret2)
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
