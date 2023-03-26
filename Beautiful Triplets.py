#Problem Link : https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

n, d = [int(r) for r in input().split()]
a = [int(r) for r in input().split()]

triplets = 0
for i in range(n-2):
    for j in range(i + 1, n-1):
        if a[j] - a[i] == d:
            foundTrip = False
            for k in range(j + 1, n):
                if a[k] - a[j] == d:
                    triplets += 1
                    foundTrip = True
                    break
            if foundTrip == True:
                break
            
print(triplets)
