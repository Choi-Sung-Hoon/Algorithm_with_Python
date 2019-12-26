import sys
from collections import deque
from queue import PriorityQueue

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for c in range(n)]

shark_r, shark_c, shark_size, eat_count = 0, 0, 2, 0
for r in range(n):
	for c in range(n):
		if board[r][c] == 9:
			shark_r, shark_c = r, c

answer = 0
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
while True:
	q = deque()
	q.appendleft([0, shark_r, shark_c])
	pq = PriorityQueue()
	visited = set([(shark_r, shark_c)])
	while q:
		dist, cur_r, cur_c = q.pop()
		
		for dr, dc in directions:
			next_r = cur_r + dr
			next_c = cur_c + dc
			
			if 0 <= next_r < n and 0 <= next_c < n:
				if (next_r, next_c) not in visited:
					# if a shark can pass
					if board[next_r][next_c] <= shark_size:
						# if the fish is eatable
						if 0 < board[next_r][next_c] < shark_size:
							pq.put((dist + 1, next_r, next_c))
						q.appendleft([dist + 1, next_r, next_c])
						visited.add((next_r, next_c))
	
	qsize = pq.qsize()
	if qsize == 0:
		break
	elif qsize > 0:
		dist, fish_r, fish_c = pq.get()
		# move shark
		board[shark_r][shark_c] = 0
		shark_r, shark_c = fish_r, fish_c
		board[shark_r][shark_c] = 9
		# eat fish
		eat_count += 1
		if eat_count == shark_size:
			shark_size += 1
			eat_count = 0
		answer += dist
print(answer)
