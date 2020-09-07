#!/bin/python3

import math
import os
import random
import re
import sys

def swap_indices(arr, ind1, ind2):
    return arr

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # copy of original array
    original_arr = arr.copy()

    # copy of working array
    original_dict = []
    for index, value in enumerate(original_arr):
        original_dict.append({"index": index, "value": value})
    print(original_dict)

    # copy of sorted array
    sorted_arr = arr.copy()
    sorted_arr.sort()

    # dict of reference values

    sorted_arr.sort()
    print(original_arr)
    print(sorted_arr)

    num_swaps = 0

    for index, value in enumerate(original_arr):
        print("original value: {} | ordered value: {}".format(original_arr[index], sorted_arr[index]))
        if original_arr[index] != sorted_arr[index]:
            # Update the number of swaps
            num_swaps += 1
            unsorted_index = 11
            original_arr[index] = index



    print(num_swaps)
    return num_swaps

if __name__ == '__main__':
    #os.environ['OUTPUT_PATH'] = '/Users/christina/PycharmProjects/hackerrank-python/output'

    #print("OUTPUT_PATH:", os.getenv['OUTPUT_PATH'])

    fptr = open(os.getenv('OUTPUT_PATH', '6_minimum_swaps_2.txt'), 'w')

    #n = int(input())

    #arr = list(map(int, input().rstrip().split()))

    # intro
    n = 7
    arr = [1, 3, 5, 2, 4, 6, 7]

    # Sample Input 0
    n = 4
    arr = [4, 3, 1, 2]

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
