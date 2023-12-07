#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arraySplitting' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def arraySplitting(arr):
    # Write your code here
    if all(a == 0 for a in arr):
        return len(arr)-1
    arr = [a for a in arr if a > 0]
    def recur(i,j):
        if i == j:
            return 0
        s = 0
        ps = []
        for k in range(i,j+1):
            s += arr[k]
            ps.append(s)
        for k,psk in enumerate(ps):
            if psk == ps[-1] - psk:
                l = recur(i,i+k)
                r = recur(i+k+1,j)
                return 1+max(l,r)
        return 0
    return recur(0,len(arr)-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = arraySplitting(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
