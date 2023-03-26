#Problem Link : https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekar_numbers = []
    for number in range(p, q + 1):
        square = str(int(math.pow(number, 2)))
        square_digits = len(square)
        right = int(square[square_digits // 2 :])
        left = 0 if square_digits == 1 else int(square[: square_digits // 2])
        if right + left == number:
            kaprekar_numbers.append(number)
    print(" ".join(map(str, kaprekar_numbers)) if len(kaprekar_numbers) != 0 else "INVALID RANGE")
