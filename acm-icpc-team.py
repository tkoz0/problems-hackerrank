#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    topic = [[bool(int(c)) for c in person] for person in topic]
    n = len(topic)
    m = len(topic[0])
    counts = dict() # num topics -> count teams
    for i in range(n):
        for j in range(i+1,n):
            topic_count = 0
            for k in range(m):
                if topic[i][k] or topic[j][k]:
                    topic_count += 1
            if topic_count not in counts:
                counts[topic_count] = 0
            counts[topic_count] += 1
    t = max(counts.keys())
    return [t,counts[t]]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
