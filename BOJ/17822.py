import sys
from collections import deque

# initialize
n, m, t = map(int, sys.stdin.readline().split())
disk = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for r in range(1, n + 1):
	line = list(map(int, sys.stdin.readline().split()))
	for c in range(1, m + 1):
		disk[r][c] = line[c - 1]


def rotate(_x, _d, _k):
	# rotate counter-clockwise
	if _d:
		# for all disks which is multiple of x
		for i in range(_x, n + 1, _x):
			temp = deque(disk[i][1:])
			temp.rotate(-(_k % m))
			disk[i][1:] = temp
	# rotate clockwise
	else:
		# for all disks which is multiple of x
		for i in range(_x, n + 1, _x):
			temp = deque(disk[i][1:])
			temp.rotate(_k % m)
			disk[i][1:] = temp


directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
for _ in range(t):
	x, d, k = map(int, sys.stdin.readline().split())
	rotate(x, d, k)
	
	found = False
	total_visited = set()
	for r in range(1, n + 1):
		for c in range(1, m + 1):
			if (r, c) not in total_visited:
				q = deque([(r, c)])
				visited = set([(r, c)])
				
				# BFS
				while q:
					cur_r, cur_c = q.pop()
					
					# for 4 adjacent numbers
					for dr, dc in directions:
						next_r = cur_r + dr
						next_c = cur_c + dc
						if 0 < next_r <= n and 0 < next_c <= m and (next_r, next_c) not in visited:
							# if it's the same number
							if disk[next_r][next_c] and disk[cur_r][cur_c] == disk[next_r][next_c]:
								q.appendleft((next_r, next_c))
								visited.add((next_r, next_c))
					# hidden condition for circular disk
					if disk[cur_r][cur_c]:
						if (cur_r, m) not in visited and cur_c == 1 and disk[cur_r][cur_c] == disk[cur_r][m]:
							q.appendleft((cur_r, m))
							visited.add((cur_r, m))
						elif (cur_r, 1) not in visited and cur_c == m and disk[cur_r][cur_c] == disk[cur_r][1]:
							q.appendleft((cur_r, 1))
							visited.add((cur_r, 1))
				
				if len(visited) > 1:
					for vr, vc in visited:
						disk[vr][vc] = 0
					found = True
				
				total_visited |= visited
					
	if not found:
		count, average = 0, 0
		for i in range(1, n + 1):
			for j in range(1, m + 1):
				if disk[i][j]:
					count += 1
					average += disk[i][j]
		
		# filter divide by zero
		if count:
			average /= count

		for i in range(1, n + 1):
			for j in range(1, m + 1):
				if disk[i][j]:
					if disk[i][j] > average:
						disk[i][j] -= 1
					elif disk[i][j] < average:
						disk[i][j] += 1
	
print(sum(map(sum, disk)))
