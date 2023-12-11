#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    y = year
    isleap = (y < 1918 and y % 4 == 0) or (y > 1918 and (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0))
    return f'26.09.{y}' if y == 1918 else (f'12.09.{y}' if isleap else f'13.09.{y}')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
