#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    for i,l in enumerate(q):
        if i+1 < l and abs(l - (i+1)) > 2:
            print('Too chaotic')
            return
    # merge sort counting inversions
    inversions = 0
    qq = [0]*len(q)
    def ms(i,j):
        nonlocal inversions
        if j-i < 2:
            return
        m = (i+j)//2
        ms(i,m)
        ms(m,j)
        k = i
        k1 = i
        k2 = m
        while k1 < m and k2 < j:
            if q[k1] < q[k2]:
                qq[k] = q[k1]
                k1 += 1
            else:
                qq[k] = q[k2]
                k2 += 1
                inversions += m-k1
            k += 1
        while k1 < m:
            qq[k] = q[k1]
            k1 += 1
            k += 1
        while k2 < j:
            qq[k] = q[k2]
            k2 += 1
            k += 1
        for k in range(i,j):
            q[k] = qq[k]
    ms(0,len(q))
    print(inversions)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
