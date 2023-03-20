#Problem Link : https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    L = len(s)
    rows = int(math.floor(L**(0.5)))
    columns = int(math.ceil(L**(0.5)))
    output = ""
    for i in range(columns):
        k = i
        for j in range(k,L,columns):
            output+=s[j]
        output+=" "
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = encryption(s)
    fptr.write(result + '\n')
    fptr.close()
