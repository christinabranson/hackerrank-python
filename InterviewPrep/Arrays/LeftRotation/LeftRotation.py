#!/bin/python3

import math
import os
import random
import re
import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Complete the rotLeft function below.
def rotLeft(a, d):

    pp.pprint(a)
    pp.pprint(d)
    for rotation in range(d):
        a.append(a.pop(0))

    pp.pprint(a)
    #a_string = ' '.join(map(str, a))
    #pp.pprint(a_string)
    return a

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', '5_left_rotation.txt'), 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    #a = [1, 2, 3, 4, 5]
    #d = 4

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
