import sys
from math import *
from heapq import *
from bisect import *
from itertools import *
from functools import *
from collections import *

def read(fn=int):
	return map(fn, input().split())

l = []
go = True
for line in sys.stdin:
	line = line.strip('\n')
	if go:
		l.append(line)
		if not line:
			go = False

			n = (len(l[-2]) + 1) // 4

			s = [[] for _ in range(n)]
			for r in l[:-2]:
				for j in range(1,len(r), 4):
					if r[j] != ' ':
						s[j//4].append(r[j])
			for i in range(n):
				s[i] = s[i][::-1]

			s2 = [c[:] for c in s]
	else:
		_,x,_,a,_,b = line.split()
		x,a,b = map(int,(x,a,b))
		a -= 1
		b -= 1

		for _ in range(x):
			s[b].append(s[a].pop())
		
		s2[b].extend(s2[a][-x:])
		s2[a] = s2[a][:-x]

print(''.join(c[-1] for c in s))
print(''.join(c[-1] for c in s2))