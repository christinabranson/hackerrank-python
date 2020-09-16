#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# NOTE: this one passes all test cases



# Complete the isValid function below.
def isValid(s):
    s_counter = Counter(s)
    s_min_count = min(s_counter.values())
    s_max_count = max(s_counter.values())

    # if all the elements occur the same number of times...
    if s_min_count == s_max_count:
        return "YES"

    # Now try removing the one at max value...
    for letter in s_counter:
        copy_counter = s_counter.copy()
        copy_counter[letter] -= 1

        copy_min_count = min([value for value in copy_counter.values() if value > 0])
        copy_max_count = max(copy_counter.values())
        if copy_min_count == copy_max_count:
            return "YES"

    return "NO"

if __name__ == '__main__':

    # YES
    s = "abc"

    # YES
    s = "abcc"

    # YES
    s = "aabbc"

    result = isValid(s)
    print(result)
