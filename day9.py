import sys
from math import *
from heapq import *
from bisect import *
from itertools import *
from functools import *
from collections import *

def read(fn=int):
	return map(fn, input().split())

def move(hp,tp):
	if abs(hp[0] - tp[0]) == abs(hp[1] - tp[1]) == 2:
		tp[0] += 1 if tp[0] < hp[0] else -1
		tp[1] += 1 if tp[1] < hp[1] else -1
		return
	if abs(hp[0] - tp[0]) > 1 or abs(hp[1] - tp[1]) > 1:
			if abs(hp[0] - tp[0]) == 2:
				tp[1] = hp[1]
				tp[0] = hp[0] + 1 if tp[0] > hp[0] else hp[0] - 1
			else:
				tp[0] = hp[0]
				tp[1] = hp[1] + 1 if tp[1] > hp[1] else hp[1] - 1


h1 = [[0,0] for _ in range(2)]
h2 = [[0,0] for _ in range(10)]
vis1 = set()
vis2 = set()
for line in sys.stdin:
	d,l = line.strip().split()
	l = int(l)

	for _ in range(l):
		match d:
			case 'R':
				h1[0][0] += 1
				h2[0][0] += 1
			case 'L':
				h1[0][0] -= 1
				h2[0][0] -= 1
			case 'U':
				h1[0][1] += 1
				h2[0][1] += 1
			case 'D':
				h1[0][1] -= 1
				h2[0][1] -= 1

		for i in range(len(h1)-1):
			move(h1[i], h1[i+1])

		for i in range(len(h2)-1):
			move(h2[i], h2[i+1])

		vis1.add(tuple(h1[-1]))
		vis2.add(tuple(h2[-1]))
print(len(vis1))
print(len(vis2))