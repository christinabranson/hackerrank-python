#!/bin/python3

import math
import os
import random
import re
import sys

import pprint

pp = pprint.PrettyPrinter(indent=4)

def get_hourglass_indices(num_rows, num_cols):
    indices = []

    return indices

# Complete the hourglassSum function below.
def hourglassSum(arr):
    pp.pprint(arr)

    num_rows = len(arr)
    num_cols = len(arr[0])

    max_value = False

    for row in range(num_rows):
        for col in range(num_cols):
            if row + 2 < num_rows and col + 2 < num_cols:
                #pp.pprint(str(row) + ", " + str(col) + ": " + str(arr[row][col]))
                value  = arr[row + 0][col + 0] + arr[row + 0][col + 1] + arr[row + 0][col + 2]  # top row
                value += arr[row + 1][col + 1]                                                  # middle row
                value += arr[row + 2][col + 0] + arr[row + 2][col + 1] + arr[row + 2][col + 2]  # top row

                pp.pprint(value)
                if max_value is False or value > max_value:
                    max_value = value

    pp.pprint(max_value)
    return max_value

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', '4_2D_Array_DS.txt'), 'w')


    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    #arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
