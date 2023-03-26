#Problem Link : https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def min_distance(ar, total_distance):
    distance = total_distance
    for i in range(len(ar)):
        for j in range(len(ar)):
            if ar[i] == ar[j] and i != j:
                cur_dist = abs(i - j)
                distance = cur_dist if cur_dist < distance else distance
                break
    return distance if distance != total_distance else -1

n = int(input().strip())
ar = [int(A_temp) for A_temp in input().strip().split(' ')]
print (min_distance(ar, n))
