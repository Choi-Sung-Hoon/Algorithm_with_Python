import sys
from collections import deque

R, C, T = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
air_purifier = list()

# find air purifier
for r in range(R):
	for c in range(C):
		if board[r][c] == -1:
			air_purifier.append((r, c))

# for a given time
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
for t in range(T):
	spread_q = deque()
	# for all dust on the map
	for r in range(R):
		for c in range(C):
			if board[r][c] > 0:
				spread_amount = board[r][c] // 5
				
				# for all directions
				for dr, dc in directions:
					next_r = r + dr
					next_c = c + dc
					# if next block is available
					if -1 < next_r < R and -1 < next_c < C:
						if board[next_r][next_c] != -1:
							board[r][c] -= spread_amount
							spread_q.appendleft((next_r, next_c, spread_amount))
	
	# spread dust
	while spread_q:
		r, c, spread_amount = spread_q.pop()
		board[r][c] += spread_amount

	# air purifier works counter-clockwise
	base_r, base_c = air_purifier[0]
	for r in range(base_r - 1, -1, -1):
			board[r][base_c] = board[r - 1][base_c]
	for c in range(C - 1):
		board[0][c] = board[0][c + 1]
	for r in range(base_r):
		board[r][C - 1] = board[r + 1][C - 1]
	for c in range(C - 1, base_c, -1):
		if board[base_r][c - 1] == -1:
			board[base_r][c] = 0
		else:
			board[base_r][c] = board[base_r][c - 1]
		
	# air purifier works clockwise
	base_r, base_c = air_purifier[1]
	for r in range(base_r + 1, R - 1, 1):
		board[r][base_c] = board[r + 1][base_c]
	for c in range(C - 1):
		board[R - 1][c] = board[R - 1][c + 1]
	for r in range(R - 1, base_r, -1):
		board[r][C - 1] = board[r - 1][C - 1]
	for c in range(C - 1, base_c, -1):
		if board[base_r][c - 1] == -1:
			board[base_r][c] = 0
		else:
			board[base_r][c] = board[base_r][c - 1]

answer = 0
for r in range(R):
	for c in range(C):
		if board[r][c] > 0:
			answer += board[r][c]
print(answer)
