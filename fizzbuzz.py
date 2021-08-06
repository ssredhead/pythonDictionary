#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    i = 1
    for i in range(1, n+1):
        if i%3 == 0:
            print("Fizz", end="")
            if i%5 == 0: 
                print("Buzz", end="")
        elif i%5 == 0:
            print("Buzz", end="")
        else:
            print(i, end="")
        print()
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
