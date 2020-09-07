#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinCost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY crew_id
#  2. INTEGER_ARRAY job_id
#

def getMinCost(crew_id, job_id):
    # Write your code here
    print("getMinCost({},{})".format(crew_id, job_id))

    job_distance = None

    sortedCrewIds = sorted(crew_id)
    sortedJobIds = sorted(job_id)
    try_one = [abs(sortedCrewIds[i] - sortedJobIds[i]) for i in range(len(sortedCrewIds))]
    return sum(try_one)


    for value in sortedCrewIds:
        if value in sortedJobIds:
            sortedCrewIds.remove(value)
            sortedJobIds.remove(value)

    print("after deletion: ")

    print(sortedCrewIds)
    print(sortedJobIds)

    return job_distance

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', 'q1.txt'), 'w')

    crew_id_count = int(input().strip())

    crew_id = []

    for _ in range(crew_id_count):
        crew_id_item = int(input().strip())
        crew_id.append(crew_id_item)

    job_id_count = int(input().strip())

    job_id = []

    for _ in range(job_id_count):
        job_id_item = int(input().strip())
        job_id.append(job_id_item)

    result = getMinCost(crew_id, job_id)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
