#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# NOTE: this one fails for something like "aabbc"

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
        if s_counter[letter] == s_max_count:
            s_counter[letter] -= 1
            break

    s_min_count = min(s_counter.values())
    s_max_count = max(s_counter.values())
    if s_min_count == s_max_count:
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
