import sys

n, k = map(int, sys.stdin.readline().split())
board_info = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
board = [[list() for _ in range(n + 1)] for _ in range(n + 1)]
chess_pieces = [0]

# initial board information
for i in range(1, n + 1):
	line = list(map(int, sys.stdin.readline().split()))
	for j in range(1, n + 1):
		board_info[i][j] = line[j - 1]

# initial chess pieces and board
for idx in range(1, k + 1):
	r, c, direction = map(int, sys.stdin.readline().split())
	chess_pieces.append([r, c, direction])
	board[r][c].append(idx)
	

# returns false if it's blue or out of boundary
def boundary_and_blue_check(_r, _c):
	if _r < 1 or _r > n or _c < 1 or _c > n:
		return False
	if board_info[_r][_c] == 2:
		return False
	return True


# returns current position if it's blue or out of boundary
def get_next_pos(_r, _c, _d):
	next_r, next_c, next_d = _r, _c, _d
	# if next position is white or red
	if boundary_and_blue_check(next_r + directions[next_d][0], next_c + directions[next_d][1]):
		next_r, next_c = next_r + directions[next_d][0], next_c + directions[next_d][1]
	# if next position is blue or out of boundary
	else:
		next_d = next_d + 1 if next_d % 2 else next_d - 1
		# if next position is white or red
		if boundary_and_blue_check(next_r + directions[next_d][0], next_c + directions[next_d][1]):
			next_r, next_c = next_r + directions[next_d][0], next_c + directions[next_d][1]
			
	return next_r, next_c, next_d


directions = ((), (0, 1), (0, -1), (-1, 0), (1, 0))
turn = 0
while turn <= 1000:
	turn += 1
	for idx, piece in list(enumerate(chess_pieces))[1:]:
		r, c, d = chess_pieces[idx][0], chess_pieces[idx][1], chess_pieces[idx][2]
		next_r, next_c, chess_pieces[idx][2] = get_next_pos(r, c, d)
		
		# no need to move chess pieces because it's blue or out of boundary
		if r == next_r and c == next_c:
			continue
		
		# split chess pieces into 2
		base_index = board[r][c].index(idx)
		board[r][c], temp_list = board[r][c][:base_index], board[r][c][base_index:]
		
		# white
		if board_info[next_r][next_c] == 0:
			# move and update position of chess pieces
			board[next_r][next_c].extend(temp_list)
			for i in temp_list:
				chess_pieces[i][0], chess_pieces[i][1] = next_r, next_c
		# red
		elif board_info[next_r][next_c] == 1:
			# move and update position of chess pieces
			board[next_r][next_c].extend(reversed(temp_list))
			for i in temp_list:
				chess_pieces[i][0], chess_pieces[i][1] = next_r, next_c
		
		if len(board[next_r][next_c]) >= 4:
			print(turn)
			sys.exit(0)
			
print(-1)
