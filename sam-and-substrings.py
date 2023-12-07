#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(n):
    # Write your code here
    '''
    d = [int(c) for c in n]
    ret = 0
    for i in range(len(d)):
        s = 0
        for j in range(i,len(d)):
            s = (10*s + d[j]) % 1000000007
            ret += s
        ret %= 1000000007
    return ret
    '''
    d = [int(c) for c in n]
    ret = 0
    p = 1
    add = 0
    for j in range(len(d)-1,-1,-1):
        add = (add + p) % 1000000007
        p = (p * 10) % 1000000007
        ret = (ret + d[j]*add*(j+1)) % 1000000007
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
