#!/bin/python3

import math
import os
import random
import re
import sys
import requests


#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#

def getNumDrawsFromJSONData(json_data, year):
    total_from_response = 0
    for datum in json_data['data']:
        print(datum)
        if int(datum['year']) == year:
            total_from_response += 1
    return total_from_response

def getShouldBreakFromJSONData(json_data, year):
    return False
    should_break = False
    for datum in json_data['data']:
        if int(datum['year']) != year:
            should_break = True
            return should_break
    return should_break

def getNumDraws(year):
    total = 0

    # Write your code here
    for goal_num in range(0,10):
        url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1goals=' + str(goal_num) + '&team2goals=' + str(goal_num) + ''
        print(url)
        response = requests.get(url)
        json_response = response.json()
        print(json_response)
        total += int(json_response['total'])

    print(total)
    return total

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', '0_sock_merchant.txt'), 'w')

    #year = int(input().strip())

    year = 2011

    result = getNumDraws(year)

    fptr.write(str(result) + '\n')

    fptr.close()
