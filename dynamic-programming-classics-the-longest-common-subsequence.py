#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestCommonSubsequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def longestCommonSubsequence(a, b):
    # Write your code here
    n = len(a)
    m = len(b)
    L = [[-1]*(m+1) for _ in range(n+1)]
    # L(i,j) = lcs of a[:i],b[:j]
    P = [['']*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        L[i][0] = 0
    for j in range(m+1):
        L[0][j] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1] == b[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
                P[i][j] = '-1,-1'
            else:
                l1 = L[i-1][j]
                l2 = L[i][j-1]
                L[i][j] = max(l1,l2)
                P[i][j] = '-1,0' if l1 > l2 else '0,-1'
    ret = []
    i,j = n,m
    while P[i][j] != '':
        if P[i][j] == '-1,0':
            i -= 1
        elif P[i][j] == '0,-1':
            j -= 1
        else:
            ret.append(a[i-1])
            i -= 1
            j -= 1
    return ret[::-1]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = longestCommonSubsequence(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
