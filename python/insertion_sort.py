#!/usr/bin/python

# # # # # # # # # #
# Insertion sort  #
# # # # # # # # # #

import sys
import timeit

def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (l[j] > key) and (j >= 0):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
    return l

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

sort_name = "Insertion sort"

if (len(sys.argv) == 2):
    word_list = read_words(sys.argv[1])
    # print 'Starting', sort_name, 'on', sys.argv[1], '...'
    start = timeit.default_timer()
    result = insertion_sort(word_list)
    stop = timeit.default_timer()
    # print 'Done. (Duration:', stop - start, 'seconds)'
    # print 'Sorted Input: ', str(result)
    print '"' + str(stop - start) + '"'
else:
    print sort_name, ': Invalid input'
