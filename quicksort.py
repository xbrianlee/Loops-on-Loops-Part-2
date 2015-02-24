#!/usr/bin/python

# # # # # # # # # # #
# Quicksort Strings #
# # # # # # # # # # #

import sys
import timeit

def qsort(arr): 
     if len(arr) <= 1:
          return arr
     else:
          return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])

print ''
print 'Starting to sort', len(sys.argv), 'items.'

start = timeit.default_timer()
result = qsort(sys.argv)
stop = timeit.default_timer()

print 'Done. (Duration:', stop - start, 'seconds)'
print 'Sorted Input: ', str(result)
print ''