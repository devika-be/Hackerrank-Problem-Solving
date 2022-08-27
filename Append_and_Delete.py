#Problem Link : https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    
    matched_occurrences=0
    
    for (char_in_s, char_in_t) in zip(s, t):
        if char_in_s==char_in_t:
            matched_occurrences+=1
            
        else:
            break
    tot_len = len(s) + len(t)

    if (2*matched_occurrences+k >= tot_len and tot_len%2==k%2) or tot_len<k:
      return "Yes"

    return "No"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
