import sys
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

# get list of viruses
virus_list = deque()
empty_rooms = 0
for i in range(n):
	for j in range(n):
		if board[i][j] == 0:
			empty_rooms += 1
		elif board[i][j] == 2:
			virus_list.appendleft((i, j))

answer = sys.maxsize - 1
# for all combinations of viruses
for selected in combinations(virus_list, m):
	q = deque()
	visited = set()
	for virus in selected:
		q.appendleft((virus, 0))
		visited.add(virus)
	
	# bfs
	infected, max_dist = 0, 0
	while q:
		cur, dist = q.pop()
		for dr, dc in directions:
			next_r = cur[0] + dr
			next_c = cur[1] + dc
			if -1 < next_r < n and -1 < next_c < n:
				if (next_r, next_c) not in visited:
					if board[next_r][next_c] != 1:
						# update distance and infection count only if virus is spread in empty room
						if board[next_r][next_c] == 0:
							infected += 1
							max_dist = max(max_dist, dist + 1)
						q.appendleft(((next_r, next_c), dist + 1))
						visited.add((next_r, next_c))
	# update answer if we succeeded in spreading virus
	if infected == empty_rooms:
		answer = min(answer, max_dist)
		
# if answer is not found
if answer == sys.maxsize - 1:
	print(-1)
# if answer is found
else:
	print(answer)
