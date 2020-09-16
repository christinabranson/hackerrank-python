#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletions_required = 0
    current_char = s[0]
    for char in range(1, len(s)):
        if s[char] == current_char:
            deletions_required += 1
        current_char = s[char]

    return deletions_required

if __name__ == '__main__':

    # 5
    s = "AAAA"

    # 4
    s = "BBBBB"

    # 0
    s = "ABABABAB"

    # 0
    s = "BABABA"

    # 4
    s = "AAABBB"

    result = alternatingCharacters(s)
    print(result)