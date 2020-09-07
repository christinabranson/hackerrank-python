#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    return_list = []

    string_dict = {}
    for string in strings:
        if string in string_dict:
            string_dict[string] += 1
        else:
            string_dict[string] = 1

    for query in queries:
        if query in string_dict:
            return_list.append(string_dict[query])
        else:
            return_list.append(0)

    return return_list

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', 'SparseArrays.txt'), 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
