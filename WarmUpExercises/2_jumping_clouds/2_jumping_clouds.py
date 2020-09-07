#!/bin/python3

import math
import os
import random
import re
import sys

import pprint

pp = pprint.PrettyPrinter(indent=4)

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    current_cloud = 0
    steps = 0
    failsafe = 0
    while current_cloud < len(c) - 1 and failsafe < 5:
        failsafe += 1

        pp.pprint("current cloud: " + str(current_cloud))
        current_cloud_2 = current_cloud + 2
        current_cloud_1 = current_cloud + 1

        if current_cloud_2 < len(c) and c[current_cloud_2] == 0:
            pp.pprint("stepping 2")
            current_cloud = current_cloud_2
            steps += 1
        elif current_cloud_1 < len(c) and c[current_cloud_1] == 0:
            pp.pprint("stepping 1")
            current_cloud = current_cloud_1
            steps += 1
        else:
            pp.pprint("nothing")


    pp.pprint(steps)

    return steps

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', '2_jumping_clouds.txt'), 'w')

    #n = int(input())
    #c = list(map(int, input().rstrip().split()))

    n = 6
    c = [0, 0, 0, 0, 1, 0]

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
