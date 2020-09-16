#!/bin/python3

# NOTE: WORKS BUT VERY INEFFICIENT

import math
import os
import random
import re
import sys
import bisect

# Function to get the median
def getMedian(sorted_list):
    if len(sorted_list) % 2 == 0:
        median_1 = (len(sorted_list) - 2) / 2
        median_2 = (len(sorted_list) - 2) / 2 + 1
        median = sorted_list[int(median_1)] + sorted_list[int(median_2)]
    else:
        median = sorted_list[math.floor(len(sorted_list)/2)]
        median = 2 * median

    #print("MEDIAN OF LIST {} is {}".format(sorted_list, median))
    return median

# Function to manage removing & adding elements
def bisectManageTrailing(trailing_days, value_to_remove, value_to_add):
    # Remove old value
    position_to_remove = bisect.bisect_left(trailing_days, value_to_remove)
    trailing_days.pop(position_to_remove)
    # Add new value
    bisect.insort(trailing_days, value_to_add)
    return trailing_days

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    num_notifications = 0

    # Initialize the trailing days list....
   # d0 = expenditure[0]
    trailing_days = []
    for init_trailing_num in expenditure[0:d]:
        bisect.insort(trailing_days, init_trailing_num)
    #print(trailing_days)

    for day in range(d,len(expenditure)):
        day_expenditure = expenditure[day]
        #trailing_days = expenditure[day - d : day]
        double_median_amount = getMedian(trailing_days)
        #print("DAY {} | DAY'S EXPENDITURES: {} | PREVIOUS {} DAYS: {} | DOUBLE MEDIAN: {}".format(day, day_expenditure, d, trailing_days, double_median_amount))
        if day_expenditure >= double_median_amount:
            num_notifications += 1

        # Now manage the sorted trailing days list
        if day + 1 < len(expenditure):
            #print("element to remove? {}".format(d0))
            bisectManageTrailing(trailing_days, expenditure[day - d], expenditure[day])
            #print(trailing_days)
        #d0 = expenditure[day - d + 1]

    return num_notifications

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #nd = input().split()
    #n = int(nd[0])
    #d = int(nd[1])
    #expenditure = list(map(int, input_vals.rstrip().split()))


    # correct answer: 1026
    d = 10122
    input_vals_file = "InterviewPrep/Sorting/ActivityNotifications/test_case_5.txt"
    with open(input_vals_file) as file:
        input_vals = file.read()
    expenditure = list(map(int, input_vals.rstrip().split()))

    # correct answer: 633
    #d = 10000
    #input_vals_file = "InterviewPrep/Sorting/ActivityNotifications/test_case_1.txt"
    #with open(input_vals_file) as file:
    #    input_vals = file.read()
    #expenditure = list(map(int, input_vals.rstrip().split()))

    # correct answer: 2
    #expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    #d = 5

    # correct answer: 0
    #expenditure = [1, 2, 3, 4, 4]
    #d = 4

    # correct answer 1
    #expenditure = [10, 20, 30, 40, 50]
    #d = 3


    result = activityNotifications(expenditure, d)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
