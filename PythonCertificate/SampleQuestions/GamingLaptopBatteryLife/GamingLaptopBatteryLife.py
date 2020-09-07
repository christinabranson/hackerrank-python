#!/bin/python3

def getBattery(events):
    charge = 50

    for event in events:
        charge += event
        if charge > 100:
            charge = 100
        elif charge < 0:
            charge = 0

    return charge

if __name__ == '__main__':

    # Sample 1 - Correct answer: 85
    arr = [10, -20, 61, -15]

    # Sample 2 - Correct answer: 90
    arr = [25, -30, 78, -10]

    # Sample 3 - Correct answer: 100
    arr = [-10, 68, 10]

    result = getBattery(arr)
    print(result)
