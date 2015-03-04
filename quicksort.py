#!/usr/bin/python

# # # # # # #
# Quicksort #
# # # # # # #

import sys
import timeit

def qsort(arr): 
     if len(arr) <= 1:
          return arr
     else:
          return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

sort_name = "Quicksort"

if (len(sys.argv) == 2):
	word_list = read_words(sys.argv[1])
	print 'Starting', sort_name, 'on', sys.argv[1], '...'
	start = timeit.default_timer()
	result = qsort(word_list)
	stop = timeit.default_timer()
	print 'Done. (Duration:', stop - start, 'seconds)'
	# print 'Sorted Input: ', str(result)
else:
	print sort_name, ': Invalid input'
