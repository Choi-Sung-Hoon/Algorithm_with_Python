import sys

movements = list(map(int, sys.stdin.readline().split()))
path_info = [
	[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0],
	[10, 13, 16, 19, 25],
	[20, 22, 24, 25],
	[30, 28, 27, 26, 25],
	[25, 30, 35, 40, 0]
]
# [i-th path, j-th block]
piece_positions = [[0, 0], [0, 0], [0, 0], [0, 0]]
piece_scores = [0, 0, 0, 0]
answer = 0


def dfs(idx):
	# termination condition
	if idx == 10:
		global answer
		answer = max(answer, sum(piece_scores))
		return answer
	
	# how many steps are going to be moved
	move = movements[idx]
	
	for i in range(4):
		# current piece position
		cur_path = piece_positions[i][0]
		cur_block = piece_positions[i][1]
		
		# if current piece finished the game
		if cur_block == len(path_info[cur_path]) - 1:
			continue
		
		next_path = cur_path
		next_block = cur_block + move
		# change path at the corner
		if cur_path == 0:
			if next_block == 5:
				next_path = 1
				next_block = 0
			elif next_block == 10:
				next_path = 2
				next_block = 0
			elif next_block == 15:
				next_path = 3
				next_block = 0
			elif next_block == 20:
				next_path = 4
				next_block = 3
		# change path at the center point
		elif cur_path < 4:
			if next_block >= len(path_info[cur_path]) - 1:
				next_path = 4
				next_block -= len(path_info[cur_path]) - 1
		
		# limit block to the last block of the path
		if next_block >= len(path_info[next_path]):
			next_block = len(path_info[next_path]) - 1
		
		# without the first & last block
		if path_info[next_path][next_block] != 0:
			# if next step is already taken
			if [next_path, next_block] in piece_positions:
				continue

		# move piece and update information
		piece_positions[i][0] = next_path
		piece_positions[i][1] = next_block
		piece_scores[i] += path_info[next_path][next_block]
		
		dfs(idx + 1)
		
		# reset piece and information
		piece_positions[i][0] = cur_path
		piece_positions[i][1] = cur_block
		piece_scores[i] -= path_info[next_path][next_block]


dfs(0)
print(answer)
