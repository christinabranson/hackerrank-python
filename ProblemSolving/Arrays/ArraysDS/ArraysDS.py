#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    return a[::-1]

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', 'ArraysDS.txt'), 'w')

    #arr_count = int(input())

    #arr = list(map(int, input().rstrip().split()))

    # Example 1
    arr = [1, 4, 3, 2]

    res = reverseArray(arr)
    print(res)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
