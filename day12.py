import sys
from math import *
from heapq import *
from bisect import *
from itertools import *
from functools import *
from collections import *

def read(fn=int):
	return map(fn, input().split())

inp = []
try:
	while True:
		inp.append(input())
except:
	pass

h = len(inp)
w = len(inp[0])
g = [[0]*w for _ in range(h)]
for i in range(h):
	s = inp[i]
	for j in range(w):
		c = s[j]
		g[i][j] = ord(c) - 97 if c.islower() else [0,25][c=='E']
		if c == 'S':
			start = (i,j)
		elif c == 'E':
			end = (i,j)

d = deque()
for i in range(h):
	for j in range(w):
		# if (i,j) == start: # part 1
		if g[i][j] == 0: # part 2
			d.append((0,(i,j)))

vis = set()
while d:
	l,(x,y) = d.popleft()
	if (x,y) == end:
		print(l)
		break
	if (x,y) in vis:
		continue
	vis.add((x,y))

	for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
		nx=x+dx
		ny=y+dy
		if nx in range(h) and ny in range(w):
			if g[nx][ny]<=g[x][y]+1:
				d.append((l+1,(nx,ny)))
