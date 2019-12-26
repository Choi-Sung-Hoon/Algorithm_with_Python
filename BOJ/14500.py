import sys
from copy import deepcopy

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
answer = 0
for i in range(n):
	for j in range(m):
		stack = list()
		visited = set()
		stack.append(((i, j), 0, board[i][j], visited))
		
		while stack:
			cur, depth, max_sum, visited = stack.pop()
			visited.add(cur)
			
			if depth == 3:
				answer = max(answer, max_sum)
				continue
				
			for (dr, dc) in directions:
				next_r = cur[0] + dr
				next_c = cur[1] + dc
				if 0 <= next_r < n and 0 <= next_c < m:
					if (next_r, next_c) not in visited:
						new_visited = deepcopy(visited)
						stack.append(((next_r, next_c), depth + 1, max_sum + board[next_r][next_c], new_visited))
		
		# for invalid blocks
		if i == 0:
			if j == 0 or j == m - 1:
				continue
		elif i == n - 1:
			if j == 0 or j == m - 1:
				continue
				
		# ㅜ
		if i == 0:
			answer = max(answer, sum((board[i][j - 1], board[i][j], board[i][j + 1], board[i + 1][j])))
		# ㅗ
		elif i == n - 1:
			answer = max(answer, sum((board[i][j - 1], board[i][j], board[i][j + 1], board[i - 1][j])))
		# ㅏ
		elif j == 0:
			answer = max(answer, sum((board[i - 1][j], board[i][j], board[i][j + 1], board[i + 1][j])))
		# ㅓ
		elif j == m - 1:
			answer = max(answer, sum((board[i - 1][j], board[i][j - 1], board[i][j], board[i + 1][j])))
		# ㅜㅗㅏㅓ
		else:
			answer = max(answer, sum((board[i][j - 1], board[i][j], board[i][j + 1], board[i + 1][j])))
			answer = max(answer, sum((board[i][j - 1], board[i][j], board[i][j + 1], board[i - 1][j])))
			answer = max(answer, sum((board[i - 1][j], board[i][j], board[i][j + 1], board[i + 1][j])))
			answer = max(answer, sum((board[i - 1][j], board[i][j - 1], board[i][j], board[i + 1][j])))
print(answer)
