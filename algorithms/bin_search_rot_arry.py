#!/usr/local/bin/python

def input():
    return raw_input()

for testcase in range(int(input())):

    array_len = int(input())

    input_array = [ int(x) for x in input().split() ]
    key = int(input())

    i = 0
    found = False
    if input_array[i] == key:
        print('{}'.format(i))
    elif key < input_array[i]: # Search backwards till rotate found
        i = array_len -1
        while i >= 0:
            if input_array[i] == key:
                print('{}'.format(i))
                found = True
            if input_array[i] >= input_array[i-1]:
                break
            i -=1
    else: # Search forward till rotate found
        while i < array_len - 1:
            if input_array[i] == key:
                print('{}'.format(i))
                found = True
            if input_array[i] <= input_array[i+1]:
                break
            i +=1
    if ~found:
        print('-1')
