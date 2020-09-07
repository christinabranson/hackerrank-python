#!/bin/python3

import math
import os
import random
import re
import sys

import pprint

pp = pprint.PrettyPrinter(indent=4)

def get_paths(this_array, base_array, all_paths):
    max_value_of_this_array = max(this_array)
    pp.pprint(max_value_of_this_array)

    if max_value_of_this_array == len(base_array) - 1:
        all_paths.append(this_array)

    else:
        if max_value_of_this_array + 2 < len(c) and base_array[max_value_of_this_array + 2] == 0:
            cloned_list = this_array.copy()
            cloned_list.append(max_value_of_this_array + 2)
            get_paths(cloned_list, base_array, all_paths)

        if max_value_of_this_array + 1 < len(c) and base_array[max_value_of_this_array + 1] == 0:
            cloned_list = this_array.copy()
            cloned_list.append(max_value_of_this_array + 1)
            get_paths(cloned_list, base_array, all_paths)

    return all_paths


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    all_paths = get_paths([0], c, [])

    smallest_path = 1000
    for sublist in all_paths:
        if len(sublist) < smallest_path:
            smallest_path = len(sublist)


    return smallest_path - 1

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', '2_jumping_clouds_2.txt'), 'w')

    n = int(input())
    c = list(map(int, input().rstrip().split()))

    #n = 6
    #c = [0, 0, 0, 0, 1, 0]

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
