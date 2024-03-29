#Problem Link : https://www.hackerrank.com/challenges/torque-and-development/problem?isFullScreen=true

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

from collections import defaultdict


def walk(g, v, used):
    used[v] = True
    count = 1

    for u in g[v]:
        if not used[u]:
            count += walk(g, u, used)

    return count


def solve():
    n, m, c_lib, c_road = map(int, input().split())
    g = defaultdict(set)

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].add(v)
        g[v].add(u)

    if c_lib <= c_road:
        return n * c_lib

    answer = 0
    used = [False] * (n + 1)

    for v in range(1, n + 1):
        if not used[v]:
            cities = walk(g, v, used)
            answer += c_lib + (cities - 1) * c_road

    return answer


def main():
    q = int(input())

    for _ in range(q):
        print(solve())


if __name__ == '__main__':
    main()
