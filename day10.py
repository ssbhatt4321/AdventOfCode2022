import sys
from math import *
from heapq import *
from bisect import *
from itertools import *
from functools import *
from collections import *

def read(fn=int):
	return map(fn, input().split())

x = 1
c = 1
l = [20,60,100,140,180,220]
a = 0
g = [[' ']*40 for _ in range(6)]
for line in sys.stdin:
	line = line.strip()

	match line.split():
		case ['noop']:
			if (c-1) % 40 in (x-1,x,x+1):
				g[(c-1)//40][(c-1)%40] = '#'

			if l and c+1 > l[0]:
				a += l[0]*x
				l.pop(0)
			c += 1
		case ['addx', v]:
			if (c-1) % 40 in (x-1,x,x+1):
				g[(c-1)//40][(c-1)%40] = '#'
			if (c) % 40 in (x-1,x,x+1):
				g[(c)//40][(c)%40] = '#'
			if l and c+2 > l[0]:
				a += l[0]*x
				l.pop(0)
			c += 2
			x += int(v)
		
print(a)
print(*[''.join(f) for f in g],sep='\n')