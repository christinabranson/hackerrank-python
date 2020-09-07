#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    #nd = input().split()

    #n = int(nd[0])

    #d = int(nd[1])

    #a = list(map(int, input().rstrip().split()))

    d = 4
    a = "1 2 3 4 5"
    a = list(map(int, a.rstrip().split()))
    print(a)
    n = len(a)

    # Tested on hackerrank with both
    # Both methods passed
    # Method 2 took less time
    METHOD = 2

    if METHOD == 1:
        # method one
        new_a = a[d:] + a[:d]
        #print(new_a)

    else:
        # method two
        new_a = a.copy()
        for iteration in range(d):
            new_a.append(new_a.pop(0))
        #print(new_a)

    print(" ".join(map(str, new_a)))
