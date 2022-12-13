import sys
from math import *
from heapq import *
from bisect import *
from itertools import *
from functools import *
from collections import *

def read(fn=int):
	return map(fn, input().split())

def good(l,r):
	if type(l) == type(r) == int:
		return 1 if l > r else -1 if l < r else 0
	if type(l) == int: l = [l]
	if type(r) == int: r = [r]
	for a,b in zip(l,r):
		if (v := good(a,b)):
			return v
	return good(len(l),len(r))

inp = [*map(eval,open('test.in','r').read().replace('\n\n','\n').strip().split('\n'))]

t = 0
for i in range(len(inp)//2):
	l = inp[2*i]
	r = inp[2*i+1]
	if good(l,r) <= 0:
		t += i+1
print(t)

inp.extend([[[2]],[[6]]])
inp.sort(key=cmp_to_key(good))
print((inp.index([[2]])+1)*(inp.index([[6]])+1))