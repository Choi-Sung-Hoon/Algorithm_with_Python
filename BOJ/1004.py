import sys

t = int(sys.stdin.readline())
for _ in range(t):
	x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
	n = int(sys.stdin.readline())
	
	planet_list = list()
	result = set()
	for _ in range(n):
		planet_list.append(list(map(int, sys.stdin.readline().split())))
	
	count = 0
	for x, y, r in planet_list:
		d1 = (x1 - x)**2 + (y1 - y)**2
		d2 = (x2 - x)**2 + (y2 - y)**2
		rr = r**2
		
		if d1 < rr < d2 or d2 < rr < d1:
			count += 1
	print(count)
