#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Week4 assignment4
#Lang | 9/21/2020 | The basics(step by stepish) are already in the text,
# time module was already introduced last week,
# It is a bit easier, in a sense it gives you confident and comfort but still not easy at all for me.
# Part1. Search Algorithm Comparison

import time
import random


def sequential_search (a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    end = time.time()
    running_time = end - start

    return running_time, found


def ordered_sequential_search (a_list, item):
    a_list.sort()
    start  = time.time()
    pos = 0
    found = False
    done  = False

    while pos < len(a_list) and not found and not done:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                done = True
            else:
                pos += 1

    end = time.time()
    running_time = end  - start

    return running_time, found

def binary_search_iterative
    a_list.sort()
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        middle = (first + last) // 2
        if a_list[middle] == item:
            found = True

        else:
            if item < a_list[middle]:
                last  = middle - 1
            else:
                first = middel - 1

    end = time.time()
    running_time = end - start

    return running_time, found

def binary_search_recursive (a_list, item):
    a_list.sort()

    start = time.time()
    found = False

    if len(a_list) == 0:
        found = False
    else:
        middle = len(a_list) // 2

        if a_list[middle] == item:
            found = True
        else:
            if item < a_list[middle]:
                running_time, found = binary_search_recursive (a_list[middle], item)
            else:
                running_time, found = binary_search_recursive (a_list[middle +1:], item)

    end = time.time()
    running_time = end - start

    return running_time, found


def generate_random(total):
    sample = random.sample (range (0, total), total)
    return sample

#main func is the one I struggle the most with and "binary_search_recursive" is the next.
def main():
    """ To run when search_compare.py is run.
        Test four different search algorithms.

    Args:

    Returns:
         string : the total running time

    """

    input_lists = [500, 1000, 10000]
    outcome = {'Sequential Search': 0.0,
               'Ordered Sequential Search': 0.0,
               'Binary Search Interative': 0.0,
               'Binary Search Recursive': 0.0
               }

    for num in input_lists:
        i = 0

        while i < 100:
            test_list = generate_random(num)
            outcome['Sequential Search'] += sequential_search (test_list, -1) [0]
            outcome['Ordered Sequential Search'] += ordered_sequential_search (test_list, -1) [0]
            outcome['Binary Search Interative'] += binary_search_iterative (test_list, -1) [0]
            outcome['Binary Search Recursive'] += binary_search_recursive (test_list, -10 [0]
            i += 1

        print("Search results of size %s items:" %num)
        for key,value in outcome.items():
            print("%s took %10.7f seconds to run, on average" % (key, (value/100)

if __name__ == '__main__':
        main()
                                                                        
            


            
    



    
