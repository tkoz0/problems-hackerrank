#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    # Write your code here
    if sum(B) % 2 == 1:
        return 'NO'
    B = [b % 2 == 0 for b in B]
    ret = 0
    for i in range(len(B)):
        if i < len(B)-1:
            if not B[i]:
                ret += 2
                B[i] = not B[i]
                B[i+1] = not B[i+1]
        else:
            assert B[i]
    return str(ret)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
