import sys
from random import randint
import timeit
from SortAssistant import QuickSort_2_way

def IsSmall(a, b):
    return a < b

def IsBig(a, b):
    return a > b

def main():
    try:
        number = int(input("Please input a number: "))
        if number > 0 :
            params=[randint(-number,number) for x in range(number)]
            print(params)
            print("\n")
            QuickSort_2_way(params, IsBig)
            print(params)
    except:
            print("Unexpected error:")

if __name__ == '__main__':
    main()