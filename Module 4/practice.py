# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime, timedelta

# Complete the time_delta function below.
def time_delta(t1, t2):
    diff = t1 - time_delta(t2)
    return diff.total_seconds()

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

    #     fptr.write(delta + '\n')

    # fptr.close()
