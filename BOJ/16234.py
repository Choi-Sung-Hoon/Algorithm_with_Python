import sys
from collections import deque

n, L, R = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for c in range(n)]

answer = 0
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
while True:
	moved = False
	unions = set()
	# BFS
	for r in range(n):
		for c in range(n):
			if (r, c) not in unions:
				q = deque([(r, c)])
				visited = set([(r, c)])
				
				total, count = 0, 0
				while q:
					cur_r, cur_c = q.pop()
					total += board[cur_r][cur_c]
					count += 1
					
					for dr, dc in directions:
						next_r = cur_r + dr
						next_c = cur_c + dc
						if 0 <= next_r < n and 0 <= next_c < n:
							if (next_r, next_c) not in visited and (next_r, next_c) not in unions:
								# set a union
								if L <= abs(board[cur_r][cur_c] - board[next_r][next_c]) <= R:
									q.appendleft((next_r, next_c))
									visited.add((next_r, next_c))
				# migration
				if count > 1:
					result = total // count
					for row, col in visited:
						board[row][col] = result
					unions |= visited
					moved = True
	if moved:
		answer += 1
	else:
		break
print(answer)
