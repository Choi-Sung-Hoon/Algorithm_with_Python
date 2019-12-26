import sys


def move(r, c, s, d, z):
	temp_speed = s
	# minimize the steps of shark's movement
	if d == 1 or d == 2:
		temp_speed %= (2 * R) - 2
	elif d == 3 or d == 4:
		temp_speed %= (2 * C) - 2
	
	new_r, new_c, new_d = r, c, d
	for _ in range(temp_speed):
		if new_d == 1 and new_r == 1:
			new_d = 2
		elif new_d == 2 and new_r == R:
			new_d = 1
		elif new_d == 3 and new_c == C:
			new_d = 4
		elif new_d == 4 and new_c == 1:
			new_d = 3
		
		new_r += directions[new_d][0]
		new_c += directions[new_d][1]
	
	return new_r, new_c, s, new_d, z


R, C, M = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
for _ in range(M):
	r, c, s, d, z = map(int, sys.stdin.readline().split())
	board[r][c] = [s, d, z]
directions = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}


answer = 0
# 1. move fisher
for fisher_pos in range(1, C + 1, 1):
	# 2. get the nearest shark from the ground
	for r in range(1, R + 1, 1):
		if board[r][fisher_pos]:
			answer += board[r][fisher_pos][2]
			board[r][fisher_pos] = 0
			break

	# 3. move sharks
	temp_board = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
	for r in range(1, R + 1, 1):
		for c in range(1, C + 1, 1):
			if board[r][c]:
				new_r, new_c, s, d, z = move(r, c, board[r][c][0], board[r][c][1], board[r][c][2])
				
				# if sharks conflict
				if temp_board[new_r][new_c] == 0:
					temp_board[new_r][new_c] = [s, d, z]
				elif z > temp_board[new_r][new_c][2]:
					temp_board[new_r][new_c] = [s, d, z]
	board = temp_board
print(answer)
