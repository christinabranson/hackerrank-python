#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    sum = 0
    for index, price in enumerate(prices):
        if sum + price >= k:
            return index
        sum += price
    return len(prices)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #nk = input().split()
    #n = int(nk[0])
    #k = int(nk[1])
    #prices = list(map(int, input().rstrip().split()))

    k = 50
    prices = [1, 12, 5, 111, 200, 1000, 10]

    result = maximumToys(prices, k)
    print(result)

