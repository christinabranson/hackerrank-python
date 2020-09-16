from collections import Counter

string = "this is a test"
string_array = [char for char in string]
print(string_array)
string_counter = Counter(string_array)
print(string_counter)
sorted_string_array = sorted(string_array)
print(sorted_string_array)