#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

def swapNodes(indexes, queries):
    # Write your code here
    sys.setrecursionlimit(2000)
    t = dict()
    for i,(a,b) in enumerate(indexes):
        t[i+1] = (a,b)
    def doswap(n,d,k):
        if n == -1:
            return
        if d%k == 0:
            t[n] = (t[n][1],t[n][0])
        doswap(t[n][0],d+1,k)
        doswap(t[n][1],d+1,k)
    def inorder(n):
        if n == -1:
            return []
        return inorder(t[n][0]) + [n] + inorder(t[n][1])
    ret = []
    for k in queries:
        doswap(1,1,k)
        ret.append(inorder(1))
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
