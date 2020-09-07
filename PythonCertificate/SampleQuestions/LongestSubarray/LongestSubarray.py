#!/bin/python3

def longestSubarray(arr):
    max_length = 0

    for index, value in enumerate(arr):
        print("index: {}, value: {}".format(index, value))
        start_value = value

        index2 = index + 1
        new_subarray = [value]
        distinct_subarray = [value]
        broken = False
        while index2 < len(arr) and not broken:
            test_value = arr[index2]

            print(" - index2: {}, test_value: {}".format(index2, test_value))

            if len(distinct_subarray) == 1:
                if abs(test_value - start_value) > 1:
                    broken = True
            else:
                #if abs(test_value - distinct_subarray[0]) > 1 or abs(test_value - distinct_subarray[1]) > 1:
                if test_value not in distinct_subarray:
                    broken = True

            if not broken:
                new_subarray.append(test_value)
                if test_value not in distinct_subarray:
                    distinct_subarray.append(test_value)

            index2 += 1
        print(new_subarray)
        if len(new_subarray) > max_length:
            max_length = len(new_subarray)

    return max_length

if __name__ == '__main__':

    # Sample 1 - Correct answer 4
    #arr = [0,1,2,1,2,3]
    # Sample 2 - Correct answer 4
    #arr = [1,1,1,3,3,2,2]
    # Sample 3 - Correct answer 2
    arr = [5, 1, 2, 3, 4, 5]

    result = longestSubarray(arr)
    print(result)