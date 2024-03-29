#Problem Link : https://www.hackerrank.com/challenges/common-child/problem?isFullScreen=true

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def main():
    s1, s2 = input(), input()
    n, m = len(s1), len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[n][m])


if __name__ == '__main__':
    main()
