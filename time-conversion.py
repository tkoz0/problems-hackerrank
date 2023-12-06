#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    h,m,s_ = map(int,s[:-2].split(':'))
    if s[-2] == 'A' and h == 12:
        h = 0
    elif s[-2] == 'P' and h != 12:
        h += 12
    return '%02d:%02d:%02d'%(h,m,s_)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
