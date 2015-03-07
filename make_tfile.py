#!/usr/bin/python

# # # # # # # # 
# MAKE_TFILE  #
# # # # # # # # 

import sys
import random
import string
 
def random_word(n):
    result = ""
    for i in range(0,int(n)):
        result = result + random.choice(string.hexdigits)
    return result

def random_gen(new_file, number, dimension):
    for i in range(0,int(number)):
        new_file.write(random_word(dimension) + " ")

if (len(sys.argv) > 2):
    new_file = open("input.txt", "wb")
    random_gen(new_file, sys.argv[1], sys.argv[2])
    new_file.close()
else:
    print "Usage: make_tfile.py [number of words] [length of each word]"