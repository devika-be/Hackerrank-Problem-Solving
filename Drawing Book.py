#Problem Link : https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def solve(n, p):
    
    if(p<=n):
        
        return min(p//2, n//2 - p//2)

n = int(input().strip())

p = int(input().strip())

result = solve(n, p)

print(result)
