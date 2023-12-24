#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    rfreq = dict()
    for r in ranked:
        if r not in rfreq:
            rfreq[r] = 0
        rfreq[r] += 1
    rpos = dict()
    count = 0
    scores = sorted(rfreq.keys())[::-1]
    for r in scores:
        rpos[r] = count+1
        count += 1 # rfreq[r]
    #print(rfreq)
    #print(rpos)
    #print(scores)
    ret = []
    for p in player:
        lo,hi = 0,len(scores)-1
        while lo < hi:
            mid = (lo+hi)//2
            if p < scores[mid]:
                lo = mid+1
            else:
                hi = mid
        #print(p,lo,scores[lo])
        ret.append(rpos[scores[lo]])
        if p < scores[lo]:
            ret[-1] += 1
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
