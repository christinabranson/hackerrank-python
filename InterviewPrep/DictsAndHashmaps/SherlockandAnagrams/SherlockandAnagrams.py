#!/bin/python3

import math
import os
import random
import re
import sys

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):

    dict = {}
    #dict_positions = {}

    for letter_size in range(1, len(s)):
        for start in range(len(s)):
            if start+letter_size <= len(s):
                substring = s[start:start+letter_size]
                substring = ''.join(sorted(substring))
                #print("substring {} (start: {}, letter_size: {})".format(substring, start, letter_size))
                if substring in dict:
                    dict[substring] += 1
                    #dict_positions[substring].append({start, start + letter_size - 1})
                else:
                    dict[substring] = 1
                    #dict_positions[substring] = []
                    #dict_positions[substring].append({start, start+letter_size - 1})


    #print(dict)
    #print(dict_positions)
    num_anagrams = 0
    for substring in dict:
        if dict[substring] > 1:
            num_anagrams += nCr( dict[substring] , 2)
            #print(num_anagrams)
            dict[substring] = 0
        #elif dict[substring] == 1:
        #    reverseSubstring = substring[::-1]
        #    #print("{} | {}".format(substring, reverseSubstring))
        #    #print(reverseSubstring)
        #    if reverseSubstring != substring and reverseSubstring in dict:
        #        print("original string: {} | count original: {}, count reverse: {}, total: {}".format(substring, dict[substring], dict[reverseSubstring], dict[substring] + dict[reverseSubstring]))
        #        choose_value = nCr(dict[substring] + dict[reverseSubstring], 2)
        #        print(choose_value)
        #        num_anagrams += choose_value
        #        dict[reverseSubstring] = 0
        #    dict[substring] = 0

    #print(num_anagrams)

    return num_anagrams

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', 'SherlockandAnagrams.txt'), 'w')

    #q = int(input())
    q = 1

    for q_itr in range(q):
        #s = input()
        # Sample Input 0a - correct 4
        s = "abba"
        # Sample Input 0b - correct 0
        #s = "abcd"

        # Sample Input 1a - correct 3
        #s = "ifailuhkqq"
        # Sample Input 1b - correct 10
        #s = "kkkk"

        # Sample Input 2a - correct 5
        s = "cdcd"

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
