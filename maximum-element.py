#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    s = []
    ret = []
    m = [] # max element at top
    for op in operations:
        if op == '2':
            if s.pop() == m[-1]:
                m.pop()
        elif op == '3':
            ret.append(m[-1])
        else:
            i = int(op.split()[1])
            if len(m) == 0 or i >= m[-1]:
                m.append(i)
            s.append(i)
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
