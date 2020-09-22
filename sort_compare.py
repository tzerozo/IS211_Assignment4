#!/usr/bin/python
# -*- coding: utf-8 -*-

#Week4 assignment4
#Lang | 9/21/2020 |
#I couldn't fix what I'm missing (adding the docstrings...)
#Part2. Sorting Algorithm Comparison

import time
import random

def insertion_sort(a_list):
    start = time.time()

    for index in range(1, len(a_list)):

     current_value = a_list[index]
     position = index

     while position > 0 and a_list[position - 1] > current_value:
         a_list[position] = a_list[position - 1]
         position = position - 1

     a_list[position] = current_value
    
    end = time.time()
    running_time = end - start

    return running_time, a_list


def shell_sort(alist):
    start = time.time()

    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end = time.time()
    running_time = end - start

    return running_time, a_list


def gap_insertion_sort(a_list, start, gap):
    
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def python_sort(a_list):
    start = time.time()
    
    a_list.sort()
    
    end = time.time()
    running_time = end - start
    
    return running_time, a_list


def generate_random(total):  
    return random.sample(range(0, size), size)


def main():
    """To tests three different sort functions"""

    input_lists = [500, 1000, 10000]
    outcome = {
        'Insertion Sort': 0.0,
        'Shell Sort': 0.0,
        'Python Sort': 0.0
    }

    for num in input_lists:
        i = 0

        while i < 100:
            test_list = generate_random(num)
            outcome['Insertion Sort'] += insertion_sort(test_list)[0]
            outcome['Shell Sort'] += shell_sort(test_list)[0]
            outcome['Python Sort'] += python_sort(test_list)[0]
            i += 1

        print("Sort results of size %s items:" % num)
        for key, value in outcome.items():
            print("%s took %10.7f seconds to run, on average." % (key, (value/100)))
        

if __name__ == '__main__':
    main()
