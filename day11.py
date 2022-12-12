import sys
from math import *
from heapq import *
from bisect import *
from itertools import *
from functools import *
from collections import *

def read(fn=int):
	return map(fn, input().split())

n = 8
items = [deque([]) for _ in range(n)]
ops = [0] * n
mods = [0] * n
targets = [[0]*2 for _ in range(n)]

for i in range(n):
	input()

	items[i].extend(eval(input()[18:] + ','))
	ops[i] = input()[19:]
	mods[i] = int(input()[21:])
	targets[i][1] = int(input()[29:])
	targets[i][0] = int(input()[30:])

	if i < n-1:
		input()

mod = lcm(*mods)
cnts = [0] * n
for x in range(10000): # 20 for part 1
	for i in range(n):
		cnts[i] += len(items[i])
		while items[i]:
			old = items[i].popleft()
			v = eval(ops[i])
			# v //= 3 # part 1
			v %= mod # part 2
			items[targets[i][v % mods[i] == 0]].append(v)

cnts.sort()
print(cnts[-1]*cnts[-2])