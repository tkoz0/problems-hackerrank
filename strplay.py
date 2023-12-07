#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'playWithWords' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def playWithWords(s):
    # Write your code here
    n = len(s)
    P = [[0]*(i+1) for i in range(n)]
    for i in range(n):
        P[i][i] = 1
    for i in range(n-1):
        P[i+1][i] = 2 if s[i+1] == s[i] else 1
    for j in range(n-2,-1,-1):
        d = n - j
        for i in range(j):
            P[i+d][i] = max(
                P[i+d-1][i+1] + (2 if s[i+d] == s[i] else 0),
                P[i+d][i+1],
                P[i+d-1][i]
            )
    #for i,row in enumerate(P): print(' '.join('%02d'%z for z in row) + f'    {s[i]}')
    return max(P[i][0]*P[n-1][i+1] for i in range(n-1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = playWithWords(s)

    fptr.write(str(result) + '\n')

    fptr.close()
