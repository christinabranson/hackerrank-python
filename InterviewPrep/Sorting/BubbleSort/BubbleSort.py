#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    num_swaps = 0

    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                temp = a[j + 1]
                a[j + 1] = a[j]
                a[j] = temp
                num_swaps += 1

    print("Array is sorted in {} swaps.".format(num_swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a) - 1]))

if __name__ == '__main__':
    #n = int(input())
    #a = list(map(int, input().rstrip().split()))+


    # Sample Input 1
    # Array is sorted in 3 swaps.
    # First Element: 1
    # Last Element: 6
    a = [6, 4, 1]

    # Sample Input 1
    # Array is sorted in 3 swaps.
    # First Element: 1
    # Last Element: 3
    a = [3, 2, 1]

    countSwaps(a)
