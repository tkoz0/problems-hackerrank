#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    seqs = dict() # value -> index list
    for i,n in enumerate(a):
        if n not in seqs:
            seqs[n] = []
        seqs[n].append(i)
    ret = len(a)
    for v in seqs:
        for i in range(1,len(seqs[v])):
            ret = min(ret,seqs[v][i]-seqs[v][i-1])
    return -1 if ret == len(a) else ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
