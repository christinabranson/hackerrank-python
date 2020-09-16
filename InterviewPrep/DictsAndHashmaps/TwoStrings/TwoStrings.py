#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1_set = set([s for s in s1])
    s2_set = set([s for s in s2])
    if len(s1_set.intersection(s2_set)) > 0:
        return "Yes"
    return "NO"

if __name__ == '__main__':
    s1 = "hi"
    s2 = "world"

    result = twoStrings(s1, s2)
    print(result)
