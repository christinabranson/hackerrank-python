#!/bin/python3

import math
import os
import random
import re
import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Complete the countingValleys function below.
def countingValleys(n, s):
    pp.pprint(s)

    current_altitude = 0
    current_altitude_array = [0]    # not used, but possibly useful for debugging
    number_valleys = 0
    for step in s:
        if step == "U":
            new_altitude = current_altitude + 1
        else:
            new_altitude = current_altitude - 1

        current_altitude_array.append(new_altitude)

        if current_altitude == 0 and new_altitude == -1:
            number_valleys += 1

        current_altitude = new_altitude

    pp.pprint(current_altitude_array)
    pp.pprint(number_valleys)

    return number_valleys


if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', '1_counting_valleys.txt'), 'w')

    n = int(input())
    s = input()

    #n = 8
    #s = "UDDDUDUU"

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
