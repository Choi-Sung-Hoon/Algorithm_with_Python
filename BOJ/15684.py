import sys
n, m, h = map(int, sys.stdin.readline().split())
board = [[0 for c in range(n + 1)] for r in range(h + 1)]
for i in range(m):
	r, c = map(int, sys.stdin.readline().split())
	board[r][c] = 1


def solution(r, c, count):
	# termination condition
	if count == ladder:
		result = True
		for j in range(1, n + 1, 1):
			cur_col = j
			for i in range(1, h + 1, 1):
				if board[i][cur_col]:
					cur_col += 1
				elif board[i][cur_col - 1]:
					cur_col -= 1
			
			# current line starts and ends at the end of the same line
			if cur_col != j:
				result = False
				break
		
		# if current game is valid, finish recursion
		if result:
			global answer
			answer = count
		return
	
	# Brute Force
	for i in range(r, h + 1, 1):
		for j in range(1, n, 1):
			if not board[i][j - 1] + board[i][j] + board[i][j + 1]:
				# place a ladder
				board[i][j] = 1
				# recursion
				solution(i, j, count + 1)
				# set to initial state
				board[i][j] = 0


answer = sys.maxsize
for ladder in range(4):
	solution(1, 1, 0)
	# if found the minimum number of ladders
	if answer != sys.maxsize:
		break
# if answer is not in valid range, return -1
print(answer if answer <= 3 else -1)
