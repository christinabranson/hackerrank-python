#!/bin/python3

def avg_from_arguments(*argv):
    sum = 0
    n = 0
    for arg in argv:
        n += 1
        sum += arg

    return round(sum / n, 2)

def avg_from_list(arr):
    sum = 0
    n = 0
    for el in arr:
        n += 1
        sum += arg

    return round(sum / n, 2)


if __name__ == '__main__':
    input = [1, 2, 3]
