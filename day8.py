import sys
from math import *
from heapq import *
from bisect import *
from itertools import *
from functools import *
from collections import *

def read(fn=int):
	return map(fn, input().split())

g = []
for line in sys.stdin:
	line = line.strip()
	g.append([*map(int, line)])

c = 0
for i in range(len(g)):
	for j in range(len(g[0])):
		vis = False
		vis |= all(g[ii][j] < g[i][j] for ii in range(i))
		vis |= all(g[ii][j] < g[i][j] for ii in range(i+1,len(g)))
		vis |= all(g[i][jj] < g[i][j] for jj in range(j))
		vis |= all(g[i][jj] < g[i][j] for jj in range(j+1,len(g[0])))
		c += vis
print(c)


m = 0
for i in range(1,len(g)-1):
	for j in range(1,len(g[0])-1):
		v = 1
		a = 0
		for ii in range(i-1,-1,-1):
			a += 1
			if g[ii][j] >= g[i][j]:
				break
		v *= a

		a = 0
		for ii in range(i+1,len(g)):
			a += 1
			if g[ii][j] >= g[i][j]:
				break
		v *= a

		a = 0
		for jj in range(j-1,-1,-1):
			a += 1
			if g[i][jj] >= g[i][j]:
				break
		v *= a

		a = 0
		for jj in range(j+1,len(g[0])):
			a += 1
			if g[i][jj] >= g[i][j]:
				break
		v *= a

		m = max(m,v)
print(m)