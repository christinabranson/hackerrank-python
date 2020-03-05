#!/bin/python3

import math
import os
import random
import re
import sys

import pprint

pp = pprint.PrettyPrinter(indent=4)

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    pp.pprint(arr)

    num_swaps = 0
    correct_value = 1
    for index in range(len(arr)):
        if arr[index] != correct_value:
            # do a swap
            incorrect_value = arr[index]
            correct_key = arr.index(correct_value)

            arr.pop(index)                              # remove the wrong value
            arr.insert(index, correct_value)            # insert the good value in new position

            arr.pop(correct_key)                        # remove the good value in old position
            arr.insert(correct_key, incorrect_value)    # insert the wrong value into the old position

            num_swaps += 1      # increment the number of swaps

            pp.pprint(arr)

        correct_value += 1

    pp.pprint(num_swaps)
    return num_swaps

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', '6_minimum_swaps_2.txt'), 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    #n = 7
    #arr = [1, 3, 5, 2, 4, 6, 7]

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
