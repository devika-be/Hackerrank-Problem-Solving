#Problem Link : https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#Ans:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    caps = []
    for i in range(len(container)):
        caps.append( sum(container[i]) )
    #print(caps)

    typenums = []
    for i in range(len(container)):
        n = 0
        for j in range(len(container)):
            n += container[j][i]
        typenums.append(n)
    
    if sorted(caps) == sorted(typenums):
        return 'Possible'
    else:
        return 'Impossible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
