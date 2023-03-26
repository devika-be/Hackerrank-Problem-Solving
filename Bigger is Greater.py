#Problem Link : https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    for i in range(len(w)-1,0,-1):
        if w[i]>w[i-1]:
            
            s=sorted(w[i-1:])
            c=''
            for j in s:
                if j>w[i-1]:
                    c=j
                    s.remove(j)
                    break
            rep=''.join(sorted(s))
            b=w[:i-1]+c+rep
            return b
    return "no answer"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
