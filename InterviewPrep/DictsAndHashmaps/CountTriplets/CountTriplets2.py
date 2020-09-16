#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    triplet_count = 0

    if len(arr) < 3:
        return triplet_count

    for k, v in enumerate(arr):
        if v == 1 or v % r == 0:
            test_A = v
            test_1 = k

            test_B = 1





    return triplet_count

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', 'CountTriplets.txt'), 'w')

    #nr = input().rstrip().split()
    #n = int(nr[0])
    #r = int(nr[1])
    #arr = list(map(int, input().rstrip().split()))

    # Sample Input Example  - correct 2
    nr = "4 4"
    arr = "1 4 16 64"

    # Sample Input 0 - correct 2
    #nr = "4 2"
    #arr = "1 2 2 4"

    # Sample Input 1 - correct 6
    #nr = "6 3"
    #arr = "1 3 9 9 27 81"

    # Sample Input 2 - correct 4
    #nr = "5 5"
    #arr = "1 5 5 25 125"

    # Another test
    nr = "5 2"
    arr = "1 2 1 2 4"


    nr = nr.rstrip().split()
    r = int(nr[1])
    arr = list(map(int, arr.rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
