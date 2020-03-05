#!/bin/python3

# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
import math
import os
import random
import re
import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pp.pprint(ar)

    # refactor into an array
    # [10, 10, 10, 10, 20, 20, 20, 30, 50] => {10: 4, 20: 3, 30: 1, 50: 1}
    number_arr = {}
    for number in ar:
        if number in number_arr:
            number_arr[number] += 1
        else:
            number_arr[number] = 1

    pp.pprint(number_arr)

    # now calculate how many pairs we can get
    mod_arr = {}
    for key in number_arr:
        mod_arr[key] = math.floor(number_arr[key] / 2)

    pp.pprint(mod_arr)

    final_number = 0
    # now add up the numbers
    for key in mod_arr:
        final_number += mod_arr[key]

    pp.pprint(final_number)

    return final_number

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', '0_sock_merchant.txt'), 'w')

    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    #n = 10
    #ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3 ]

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()