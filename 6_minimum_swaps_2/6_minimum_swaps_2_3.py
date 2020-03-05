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

    # try removing all values that are in the correct spot to make the array smaller?
    #for index, value in enumerate(arr):
    #    if index == value - 1:
    #        arr.pop(index)

    pp.pprint(arr)

    num_swaps = 0
    for index, value in enumerate(arr):
        correct_value = min(arr)
        pp.pprint(str(index) + ": " + str(value) + "( should be: " + str(correct_value) + ")")
        if value != correct_value:
            # do a swap
            incorrect_value = value
            correct_key = arr.index(correct_value)

            arr[correct_key] = incorrect_value

            arr.pop(index)      # just remove the last value
            num_swaps += 1      # increment the number of swaps

            pp.pprint(arr)
        else:
            pp.pprint("no swap")
            pp.pprint(arr)

    pp.pprint(num_swaps)
    return num_swaps

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', '6_minimum_swaps_2.txt'), 'w')

    #n = int(input())

    #arr = list(map(int, input().rstrip().split()))

    n = 4
    arr = [4,3,1,2]

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
