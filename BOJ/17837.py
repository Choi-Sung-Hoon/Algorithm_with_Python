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

directions = ((), (0, 1), (0, -1), (-1, 0), (1, 0))
turn = 0
while turn <= 1000:
	for idx, piece in list(enumerate(chess_pieces))[1:]:
		r, c, direction = piece[0], piece[1], piece[2]
		next_r = r + directions[direction][0]
		next_c = c + directions[direction][1]
		
		# split current chess pieces
		base_index = board[r][c].index(idx)
		board[r][c], temp_list = board[r][c][:base_index], board[r][c][base_index:]
		
		if 0 < next_r <= n and 0 < next_c <= n:
			# white
			if board_info[next_r][next_c] == 0:
				board[next_r][next_c].extend(temp_list)
				for i in temp_list:
					chess_pieces[i][0] = next_r
					chess_pieces[i][1] = next_c
			# red
			elif board_info[next_r][next_c] == 1:
				board[next_r][next_c].extend(reversed(temp_list))
				for i in temp_list:
					chess_pieces[i][0] = next_r
					chess_pieces[i][1] = next_c
			# blue
			elif board_info[next_r][next_c] == 2:
				next_dir = direction + 1 if direction % 2 else direction - 1
				next_r = r + directions[next_dir][0]
				next_c = c + directions[next_dir][1]
				
				if board_info[next_r][next_c] != 2:
					board[next_r][next_c].extend(temp_list)
					for i in temp_list:
						chess_pieces[i][0] = next_r
						chess_pieces[i][1] = next_c
				else:
					board[r][c].extend(temp_list)
		# out of border
		else:
			next_dir = direction + 1 if direction % 2 else direction - 1
			next_r = r + directions[next_dir][0]
			next_c = c + directions[next_dir][1]
			
			if board_info[next_r][next_c] != 2:
				board[next_r][next_c].extend(temp_list)
				for i in temp_list:
					chess_pieces[i][0] = next_r
					chess_pieces[i][1] = next_c
			else:
				board[r][c].extend(temp_list)
	
	turn += 1
	if len(board[next_r][next_c]) == 4:
		break
		
print(turn if turn <= 1000 else -1)
