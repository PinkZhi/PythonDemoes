import sys
from random import randint
import timeit
from SortHandler import *

def IsSmall(a, b):
    return a < b

def IsBig(a, b):
    return a > b

def Compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

def main():
    try:
        number = int(input("Please input a number: "))
        if number > 0 :
            params=[randint(-number,number) for x in range(number)]
            print(params)
            print("\n")
            sortHandler = SortHandler() 
            #sortHandler.QuickSort2(params, IsBig)
            sortHandler.QuickSort3(params, Compare)
            print(params)
    except:
            print("Unexpected error:")

if __name__ == '__main__':
    main()