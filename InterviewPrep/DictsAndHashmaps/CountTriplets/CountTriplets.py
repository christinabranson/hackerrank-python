#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    if len(arr) < 3:
        return 0

    count_dict = {}
    count_dict_positions = {}
    for index, number in enumerate(arr):
        if number in count_dict:
            count_dict[number] += 1
            count_dict_positions[number].append(index)
        else:
            count_dict[number] = 1
            count_dict_positions[number] = []
            count_dict_positions[number].append(index)

    print(count_dict_positions)

    if r == 1 and 1 in count_dict:
        return count_dict[1]

    triplet_count = 0
    for number in count_dict:
        # these are the three values we need in each triplet
        a = number
        b = a * r**1
        c = a * r**2

        # note: we obvs know a is in the dict...
        if b in count_dict and c in count_dict:
            print("values: [{}, {}, {}]: counts: [{}, {}, {}]".format(a, b, c, count_dict[a], count_dict[b], count_dict[c]))
            number_of_paths = count_dict[a] * count_dict[b] * count_dict[c]
            print("number of paths: {}".format(number_of_paths))
            triplet_count += number_of_paths

    print(triplet_count)
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
    #nr = "5 2"
    #arr = "1 2 1 2 4"


    nr = nr.rstrip().split()
    r = int(nr[1])
    arr = list(map(int, arr.rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
