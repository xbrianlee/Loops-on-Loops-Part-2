#!/usr/bin/python

# # # # # # #  
# Mergesort #
# # # # # # #  

import sys
import timeit
from heapq import merge
 
def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

sort_name = "Mergesort"

if (len(sys.argv) == 2):
	word_list = read_words(sys.argv[1])
	# print 'Starting', sort_name, 'on', sys.argv[1], '...'
	start = timeit.default_timer()
	result = merge_sort(word_list)
	stop = timeit.default_timer()
	# print 'Done. (Duration:', stop - start, 'seconds)'
	# print 'Sorted Input: ', str(result)
    print '"' + str(stop - start) + '"'
else:
	print sort_name, ': Invalid input'
