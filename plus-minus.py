#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    p = sum(1 for a in arr if a > 0)/n
    m = sum(1 for a in arr if a < 0)/n
    z = sum(1 for a in arr if a == 0)/n
    print('%.6f\n%.6f\n%.6f'%(p,m,z))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
