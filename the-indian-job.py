#!/bin/python3

import os
import sys

#
# Complete the indianJob function below.
#
def indianJob(g, arr):
    #
    # Write your code here.
    #
    n = len(arr)
    sums = set([0])
    for r in arr:
        sums2 = {r+s for s in sums}
        sums |= sums2
    s = sum(arr)
    return 'YES' if min(max(z,s-z) for z in sums) <= g else 'NO'
    '''
    par1sum = 0
    par2sum = 0
    arr = sorted(arr,key=lambda x:-x)
    for r in arr:
        if par1sum < par2sum:
            par1sum += r
        else:
            par2sum += r
    return 'YES' if max(par1sum,par2sum) <= g else 'NO'
    '''
    '''
    n = len(arr)
    arr = sorted(arr, key=lambda x:-x)
    mins = 0
    r1 = 0
    r2 = 0
    i = 0
    while i < n:
        z = min(r1,r2)
        r1 -= z
        r2 -= z
        mins += z
        if r1 == 0:
            r1 = arr[i]
        else:
            r2 = arr[i]
        i += 1
        if i < n:
            if r1 == 0:
                r1 = arr[i]
                i += 1
            elif r2 == 0:
                r2 = arr[i]
                i += 1
    return 'YES' if mins + max(r1,r2) <= g else 'NO'
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ng = input().split()

        n = int(ng[0])

        g = int(ng[1])

        arr = list(map(int, input().rstrip().split()))

        result = indianJob(g, arr)

        fptr.write(result + '\n')

    fptr.close()
