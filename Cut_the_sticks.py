#Problem Link : https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
while len(arr)>=1:
    print(len(arr))
    minm=min(arr)    
    arr=[temp-minm for temp in arr if (temp-minm)>0]
