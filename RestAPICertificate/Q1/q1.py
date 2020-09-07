#!/bin/python3

import math
import os
import random
import re
import sys
import requests
import json



#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

def getTotalFromJson(json_data, team, year):
    total_from_response = 0
    for datum in json_data['data']:
        if int(datum['year']) == year:
            if team == 1:
                total_from_response += int(datum['team1goals'])
            else:
                total_from_response += int(datum['team2goals'])
    return total_from_response

def getTotalGoals(team, year):
    import requests
    # Write your code here
    total_goals = 0

    # home team
    url = 'https://jsonmock.hackerrank.com/api/football_matches?year' + str(year) + '&team1=' + team
    response = requests.get(url)
    json_response = response.json()
    total_pages = int(json_response['total_pages'])
    print("TOTAL PAGES {}".format(total_pages))
    total_goals += getTotalFromJson(json_response, 1, year)
    page = 2
    while page <= total_pages:
        new_url = url + '&page=' + str(page)
        print(new_url)
        response = requests.get(new_url)
        json_response = response.json()
        total_goals += getTotalFromJson(json_response, 1, year)
        page += 1
    print(total_goals)

    # away team
    url = 'https://jsonmock.hackerrank.com/api/football_matches?year' + str(year) + '&team2=' + team
    response = requests.get(url)
    json_response = response.json()
    total_pages = int(json_response['total_pages'])
    total_goals += getTotalFromJson(json_response, 2, year)
    page = 2
    while page <= total_pages:
        new_url = url + '&page=' + str(page)
        print(new_url)
        response = requests.get(new_url)
        json_response = response.json()
        total_goals += getTotalFromJson(json_response, 2, year)
    print(total_goals)
    return total_goals

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', '0_sock_merchant.txt'), 'w')

    #team = input()
    #year = int(input().strip())

    # Sample 1 - Expected output 35
    team="Barcelona"
    year=2011

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')

    fptr.close()
