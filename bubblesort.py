#!/usr/bin/python

# # # # # # # # 
# Bubblesort  #
# # # # # # # # 

import sys
import timeit

def bubbleSort(arr):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

sort_name = "Bubblesort"

if (len(sys.argv) == 2):
	word_list = read_words(sys.argv[1])
	print 'Starting', sort_name, 'on', sys.argv[1], '...'
	start = timeit.default_timer()
	result = bubbleSort(word_list)
	stop = timeit.default_timer()
	print 'Done. (Duration:', stop - start, 'seconds)'
	# print 'Sorted Input: ', str(result)
else:
	print sort_name, ': Invalid input'
