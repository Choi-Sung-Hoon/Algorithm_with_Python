import sys

n, m, r, c, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for r in range(n)]
move_list = list(map(int, sys.stdin.readline().split()))
dice = [0, 0, 0, 0, 0, 0]


def roll(dice, direction):
	if direction == 1:
		temp = dice[5]
		dice[5] = dice[3]
		dice[2:4] = dice[1:3]
		dice[1] = temp
	elif direction == 2:
		temp = dice[5]
		dice[5] = dice[1]
		dice[1:3] = dice[2:4]
		dice[3] = temp
	elif direction == 3:
		temp = dice[0]
		dice[0] = dice[2]
		dice[2] = dice[4]
		dice[4] = dice[5]
		dice[5] = temp
	elif direction == 4:
		temp = dice[5]
		dice[5] = dice[4]
		dice[4] = dice[2]
		dice[2] = dice[0]
		dice[0] = temp
	# return top and bottom of the dice
	return dice[2], dice[5]


directions = ((), (0, 1), (0, -1), (-1, 0), (1, 0))
cur = (r, c)
for move in move_list:
	next_r = cur[0] + directions[move][0]
	next_c = cur[1] + directions[move][1]
	
	# skip this movement
	if next_r < 0 or next_r >= n or next_c < 0 or next_c >= m:
		continue
	
	# roll the dice
	roll(dice, move)
	if board[next_r][next_c] == 0:
		board[next_r][next_c] = dice[5]
	else:
		dice[5] = board[next_r][next_c]
		board[next_r][next_c] = 0
	print(dice[2])
	cur = (next_r, next_c)
