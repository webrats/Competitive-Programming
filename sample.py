#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def decryptPassword(s):
    try:
        while("*" in s):
            i = s.index("*")
            print(i)
            s[i] = 0
        print(s)
    except:
        pass


if __name__ == '__main__':

    s = input()

    result = decryptPassword(s)

    print(result)
