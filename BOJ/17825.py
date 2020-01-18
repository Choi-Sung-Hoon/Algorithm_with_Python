import sys

movements = list(map(int, sys.stdin.readline().split()))
path_info = [
	[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 0],
	[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 27, 26, 25, 30, 35, 40, 0],
	[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30, 35, 40, 0],
	[0, 2, 4, 6, 8, 10, 13, 16, 19, 25, 30, 35, 40, 0]
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
		
		# change path at the corner
		next_block = cur_block + move
		next_path = cur_path
		if cur_path < 3 and next_block == 5:
			next_path = 3
		elif cur_path < 2 and next_block == 10:
			next_path = 2
		elif cur_path < 1 and next_block == 15:
			next_path = 1
		
		# if next step is already taken
		if [next_path, next_block] in piece_positions:
			continue
		
		# move piece and update information
		if next_block >= len(path_info[next_path]):
			next_block = len(path_info[next_path]) - 1
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
