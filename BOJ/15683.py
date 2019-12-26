import sys
from copy import deepcopy

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for c in range(n)]


def up(temp_board, r, c):
	count = 1
	for i in range(r, -1, -1):
		if temp_board[i][c] == 6:
			break
		temp_board[i][c] = -1
	return count


def right(temp_board, r, c):
	count = 1
	for j in range(c, m, 1):
		if temp_board[r][j] == 6:
			break
		temp_board[r][j] = -1
	return count


def down(temp_board, r, c):
	count = 1
	for i in range(r, n, 1):
		if temp_board[i][c] == 6:
			break
		temp_board[i][c] = -1
	return count


def left(temp_board, r, c):
	count = 1
	for j in range(c, -1, -1):
		if temp_board[r][j] == 6:
			break
		temp_board[r][j] = -1
	return count


def solution(idx, obs_list):
	global answer
	temp_board = deepcopy(board)
	if idx == list_size:
		# count all detection area
		for ((r, c), observer, offset) in obs_list:
			if observer == 1:
				if offset == 0:
					right(temp_board, r, c)
				elif offset == 1:
					down(temp_board, r, c)
				elif offset == 2:
					left(temp_board, r, c)
				else:
					up(temp_board, r, c)
			elif observer == 2:
				if offset == 0 or offset == 2:
					right(temp_board, r, c)
					left(temp_board, r, c)
				elif offset == 1 or offset == 3:
					up(temp_board, r, c)
					down(temp_board, r, c)
			elif observer == 3:
				if offset == 0:
					up(temp_board, r, c)
					right(temp_board, r, c)
				elif offset == 1:
					right(temp_board, r, c)
					down(temp_board, r, c)
				elif offset == 2:
					down(temp_board, r, c)
					left(temp_board, r, c)
				else:
					left(temp_board, r, c)
					up(temp_board, r, c)
			elif observer == 4:
				if offset == 0:
					up(temp_board, r, c)
					right(temp_board, r, c)
					down(temp_board, r, c)
				elif offset == 1:
					right(temp_board, r, c)
					down(temp_board, r, c)
					left(temp_board, r, c)
				elif offset == 2:
					down(temp_board, r, c)
					left(temp_board, r, c)
					up(temp_board, r, c)
				else:
					left(temp_board, r, c)
					up(temp_board, r, c)
					right(temp_board, r, c)
			else:
				up(temp_board, r, c)
				right(temp_board, r, c)
				left(temp_board, r, c)
				down(temp_board, r, c)
				
		# get the minimum space
		count = 0
		for r in range(n):
			for c in range(m):
				if temp_board[r][c] == 0:
					count += 1
		answer = min(answer, count)
		return answer

	# traverse all occasion
	for i in range(4):
		obs_list[idx][2] = i
		solution(idx + 1, obs_list)


# make a list of observers
observer_list, list_size = list(), 0
for i in range(n):
	for j in range(m):
		if 0 < board[i][j] < 6:
			observer_list.append([(i, j), board[i][j], 0])
			list_size += 1

answer = sys.maxsize
solution(0, observer_list)
print(answer)
