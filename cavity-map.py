#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    newgrid = [list(map(int,r)) for r in grid]
    cavities = []
    for r in range(1,len(newgrid)-1):
        for c in range(1,len(newgrid[r])-1):
            a = newgrid[r][c]
            if newgrid[r-1][c] < a and newgrid[r+1][c] < a and newgrid[r][c-1] < a and newgrid[r][c+1] < a:
                cavities.append((r,c))
    for r,c in cavities:
        newgrid[r][c] = 'X'
    return [''.join(map(str,r)) for r in newgrid]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
