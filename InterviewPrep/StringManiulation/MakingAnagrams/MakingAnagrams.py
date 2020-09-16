#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):

    a_counter = Counter(a)
    b_counter = Counter(b)

    aMb = a_counter - b_counter
    bMa = b_counter - a_counter

    return sum((aMb).values()) + sum((bMa).values())


if __name__ == '__main__':

    # correct answer: 4
    a = "cde"
    b = "abc"

    # correct answer: 30
    a = "fcrxzwscanmligyxyvym"
    b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"

    res = makeAnagram(a, b)
    print(res)