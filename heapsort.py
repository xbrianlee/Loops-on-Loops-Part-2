#!/usr/bin/python

# # # # # # #  
# Heapsort  #
# # # # # # #  

import sys
import timeit

def heapsort(lst):
  for start in range((len(lst)-2)/2, -1, -1):
    siftdown(lst, start, len(lst)-1)
 
  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst
 
def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

sort_name = "Heapsort"

if (len(sys.argv) == 2):
	word_list = read_words(sys.argv[1])
	print 'Starting', sort_name, 'on', sys.argv[1], '...'
	start = timeit.default_timer()
	result = heapsort(word_list)
	stop = timeit.default_timer()
	print 'Done. (Duration:', stop - start, 'seconds)'
	# print 'Sorted Input: ', str(result)
else:
	print sort_name, ': Invalid input'
