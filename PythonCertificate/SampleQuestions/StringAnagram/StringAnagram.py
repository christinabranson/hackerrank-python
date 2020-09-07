#!/bin/python3

def getAnagrams(dictionary, queries):
    anagram_counts = []

    sorted_dictionary = {}
    for word in dictionary:
        sorted_word = "".join(sorted(word))
        if sorted_word in sorted_dictionary:
            sorted_dictionary[sorted_word] += 1
        else:
            sorted_dictionary[sorted_word] = 1
    print(sorted_dictionary)

    for query in queries:
        sorted_word = "".join(sorted(query))
        if sorted_word in sorted_dictionary:
            anagram_counts.append(sorted_dictionary[sorted_word])
        else:
            anagram_counts.append(0)

    return anagram_counts

if __name__ == '__main__':

    # Sample 1 - Correct answer: 85
    dictionary = ["hack", "a", "rank", "khac", "ackh", "kran", "rankhacer", "a", "ab", "ba", "stairs", "raits"]
    query = ["a", "nark", "bs", "hack", "stairs"]


    result = getAnagrams(dictionary, query)
    print(result)