#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    ret = -1
    drives = sorted(drives)
    for kb in keyboards:
        maxdrive = b - kb
        i,j = 0,len(drives)-1
        while i != j:
            m = (i+j)//2
            if drives[m] <= maxdrive:
                i = m+1
            else:
                j = m
        if kb + drives[i] <= b:
            ret = max(ret,kb+drives[i])
        if i > 0 and kb + drives[i-1] <= b:
            ret = max(ret,kb+drives[i-1])
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
