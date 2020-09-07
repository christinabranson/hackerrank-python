#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    #print(queries)
    lastAnswer = 0
    sequenceList = [ [] for _ in range(n) ]
    print(sequenceList)
    returnVals = []

    for query in queries:
        type    = query[0]
        x       = query[1]
        y       = query[2]

        index = (x ^ lastAnswer) % n
        print(index)

        if type == 1:
            sequenceList[index].append(y)
        else:
            sequence = sequenceList[index]
            size = len(sequence)
            lastAnswerIndex = y % size
            lastAnswer = sequence[lastAnswerIndex]
            #print(lastAnswer)
            returnVals.append(lastAnswer)


        debugString = "lastAnswer={}, sequence={}".format(lastAnswer, sequenceList)
        print(debugString)

    return returnVals


if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', 'DynamicArray.txt'), 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
