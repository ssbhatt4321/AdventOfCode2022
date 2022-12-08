import sys
from math import *
from heapq import *
from bisect import *
from itertools import *
from functools import *
from collections import *

def read(fn=int):
	return map(fn, input().split())

m = []
v = 0
for line in sys.stdin:
    line = line.strip()
    if not line:
        heappush(m,v)
        v = 0
    else:
        v += int(line)
m.sort()
print(m[-1])
print(sum(m[-3:]))