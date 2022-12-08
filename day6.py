import sys
from math import *
from heapq import *
from bisect import *
from itertools import *
from functools import *
from collections import *

def read(fn=int):
	return map(fn, input().split())

s = input()

i = 4
while len(set(s[i-4:i])) != 4:
    i += 1
print(i)

i = 14
while len(set(s[i-14:i])) != 14:
    i += 1
print(i)