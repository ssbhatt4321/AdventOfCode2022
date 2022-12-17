import sys
from math import *
from heapq import *
from bisect import *
from itertools import *
from functools import *
from collections import *
from re import *

def read(fn=int):
	return map(fn, input().split())

states = [[[-1] * (1 << 15) for _ in range(31)] for _ in range(16)]

def rec(posi, time, perm_mask):
	if states[posi][time][perm_mask] != -1:
		return states[posi][time][perm_mask]

	if time <= 1: return 0
	ans = 0
	pos = perm[posi]
	for j in range(nz):
		i = perm[j]
		if (perm_mask >> j) & 1 == 0:
			time -= dist[pos][i]
			if time <= 0:
				time += dist[pos][i]
				continue
			ans = max(ans, rec(j, time-1, perm_mask | (1 << j)) + val[i] * (time-1))
			time += dist[pos][i]
	
	states[posi][time][perm_mask] = ans
	return ans

adj = []
val = []
poss = []
for line in sys.stdin:
	line = line.strip().split()
	poss.append(line[1])
	adj.append([])
	for s in line[9:-1]:
		adj[-1].append(s[:-1])
	adj[-1].append(line[-1])
	val.append(int(line[4][5:-1]))

inds = {}
for i,pos in enumerate(poss):
	inds[pos] = i

n = len(poss)
dist = [[1000]*n for _ in range(n)]
for i in range(n):
	dist[i][i] = 0
	for neigh in adj[i]:
		dist[i][inds[neigh]] = 1

for k in range(n):
	for i in range(n):
		for j in range(n):
			dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

perm = []
for i in range(n):
	if val[i]:
		perm.append(i)
perm.append(inds['AA'])
nz = len(perm) - 1

print(rec(len(perm)-1, 30, 0))

ans = 0
for i in range(1 << nz):
	ans = max(ans, rec(len(perm)-1, 26, i) + rec(len(perm)-1, 26, ((1 << nz) - 1) & ~i))
print(ans)