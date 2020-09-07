
#!/bin/python3

import math
import os
import random
import re
import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Complete the repeatedString function below.
def repeatedString(s, n):
    pp.pprint(s)

    num_A_in_repeated_string = 0

    # get number of occurances in regular string
    num_A_in_original_string = len([x for x, v in enumerate(s) if v == 'a'])

    # now we need to figure out how instances of a regular string can fit in a
    num_instances = n / len(s)
    pp.pprint(num_instances)
    floor_num_instances = math.floor(num_instances)

    num_A_in_repeated_string = num_A_in_original_string * floor_num_instances

    # now we need to calculate in the remainder
    mod_num_instances = num_instances - floor_num_instances
    num_characters_in_mod = round(mod_num_instances * len(s))
    if num_characters_in_mod > 0:
        pp.pprint(mod_num_instances)
        pp.pprint(num_characters_in_mod)

        leftover_string = s[:num_characters_in_mod]
        num_A_in_leftover_string = len([x for x, v in enumerate(leftover_string) if v == 'a'])
        num_A_in_repeated_string += num_A_in_leftover_string

    # now
    pp.pprint(num_A_in_repeated_string)
    return num_A_in_repeated_string


if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', '3_repeated_string.txt'), 'w')

    s = input()
    n = int(input())

    #s = "a"
    #n = 1000000000000

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
