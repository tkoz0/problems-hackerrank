#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankCity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY A as parameter.
#

def hackerrankCity(A):
    # Write your code here
    # start with single vertex, generate trees TT from T
    MOD = 10**9 + 7
    N = 1 # num vertices
    D = 0 # diameter
    Y = 0 # path sums from a corner node of T
    Z = 0 # path sums across cut | between T-|-T
    T = 0 # total path sums
    for a in A: # go from tree T to tree TT
        NN = (4*N + 2) % MOD # 4 copies, 2 new vertices
        DD = (2*D + 3*a) % MOD # diameter doubles + length in middle
        YY = (4*Y # path sums toward all vertices in Ts
            + N*(3*D + 8*a) # count new T diameter + new edges used
            + (2*D + 3*a) # distance to new vertices
            ) % MOD
        ZZ = (16*Z # between Ts with edges in Ts
            + N*N*(24*D + 64*a) # middle edges used for pairwise Ts
            + (4*YY + 2*NN*(2*D + 3*a)) # new node to other side
            - (8*D + 12*a) # subtract between new nodes, counted twice
            ) % MOD
        TT = (6*Z # pairwise within Ts
            + (N*N*16*a) # middle edges used crossing Ts
            + (a) # edge connecting new nodes
            + (8*Y + 12*N*a) # new nodes to those in Ts
            + (4*T) # paths within Ts
            ) % MOD
        N,D,Y,Z,T = NN,DD,YY,ZZ,TT
    return T

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    A_count = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    result = hackerrankCity(A)

    fptr.write(str(result) + '\n')

    fptr.close()
