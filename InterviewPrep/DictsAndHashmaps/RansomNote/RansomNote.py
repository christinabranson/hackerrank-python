#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    magazine_arr = magazine
    note_att = note

    magazine_dict = {}
    for word in magazine_arr:
        if word in magazine_dict:
            magazine_dict[word] += 1
        else:
            magazine_dict[word] = 1

    note_dict = {}
    for word in note_att:
        if word in note_dict:
            note_dict[word] += 1
        else:
            note_dict[word] = 1
    print(magazine_dict)
    print(note_dict)

    #print(magazine_arr)
    #print(note_att)

    for word in note_dict:
        if word in magazine_dict:
            if magazine_dict[word] < note_dict[word]:
                return "No"
        else:
            return "No"

    return "Yes"

if __name__ == '__main__':
    #mn = input().split()
    #m = int(mn[0])
    #n = int(mn[1])
    #magazine = input().rstrip().split()
    #note = input().rstrip().split()

    # Sample Input 0
    magazine = "give me one grand today night"
    note = "give one grand today"

    # Sample Input 1
    magazine = "two times three is not four"
    note = "two times two is four"

    # Sample Input 2
    magazine = "ive got a lovely bunch of coconuts"
    note = "ive got some coconuts"

    magazine = magazine.rstrip().split()
    note = note.rstrip().split()

    return_value = checkMagazine(magazine, note)
    print(return_value)
