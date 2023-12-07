#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    arr = [0]*(n+1)
    for a,b,k in queries:
        arr[a-1] += k
        arr[b] -= k
    best = 0
    curr = 0
    for a in arr:
        curr += a
        best = max(best,curr)
    return best
    '''
    totals = dict()
    siz = 1
    while siz <= n:
        for a in range(1,n+1,siz):
            totals[(a,min(a+siz-1,n))] = 0
        siz *= 2
    siz //= 2
    #print('siz',siz)
    #print(totals)
    def count(a,b,k):
        #print(a,b,k)
        nonlocal totals,siz
        if (a,b) in totals:
            totals[(a,b)] += k
        else:
            s = siz
            while b%s != 0 or b-s+1 <= a:
                s //= 2
            count(a,b-s,k)
            count(b-s+1,b,k)
    for a,b,k in queries:
        count(a,b,k)
    #print(totals)
    def findmax(a,b,s):
        if a == b:
            return 0
        elif a+s-1 < b:
            t1 = totals[(a,a+s-1)] + findmax(a,a+s-1,s//2)
            t2 = totals[(a+s,b)] + findmax(a+s,b,s//2)
            return max(t1,t2)
        else:
            return findmax(a,b,s//2)
    ret = findmax(1,siz,siz//2) + totals[(1,siz)]
    if siz < n:
        ret = max(ret,findmax(siz+1,n,siz//2)+totals[(siz+1,n)])
    return ret
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
