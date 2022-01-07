"""
Write a program for counting the number of every character of a given text file.
"""

import pprint
import collections

with open('sample.txt','r') as f:
    count_data = collections.Counter(f.read().upper())
    count_value = pprint.pformat(count_data) # This line will display the solution in standard way
print(count_value)