#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoSubsequences' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER r
#  3. INTEGER s
#

def twoSubsequences(x, r, s):
    # Write your code here
    m = len(x)
    M = 10**9+7
    h = (r+s)//2
    l = (r-s)//2
    if (r+s)%2 == 1 or (r-s)%2 == 1 or r == 0 or r-s<0:
        return 0
    dp = [[0]*(m+1) for _ in range(h+1)]
    dp[0][0] = 1
    if x[0] <= h:
        dp[x[0]][1] = 1
    for i in range(1,m):
        #for k in range(1,m+1):
        #    dp[0][k] = 0
        for j in range(h,0,-1):
            #dp[j][0] = 0
            for k in range(1,m+1):
                if j >= x[i]:
                    dp[j][k] += dp[j-x[i]][k-1]
                    dp[j][k] %= M
    ret = 0
    for i in range(1,m+1):
        ret += dp[h][i]*dp[l][i]
        ret %= M
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    r = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    x = list(map(int, input().rstrip().split()))

    result = twoSubsequences(x, r, s)

    fptr.write(str(result) + '\n')

    fptr.close()
