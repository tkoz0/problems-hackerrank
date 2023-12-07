#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack = []
    for c in s:
        if c in '({[':
            stack.append(c)
        else:
            if len(stack) == 0:
                return 'NO'
            else:
                d = stack.pop()
                if d+c not in ['()','{}','[]']:
                    return 'NO'
    return 'YES' if len(stack) == 0 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
