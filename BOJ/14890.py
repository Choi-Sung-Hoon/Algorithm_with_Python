n, l = map(int, input().split())
board = [list(map(int, input().split())) for c in range(n)]
board2 = list(list(r) for r in zip(*board))
	
answer = 0
for i in range(n):
	
	# horizontal traverse
	j, count = 0, 1
	flag = True
	while j + 1 < n:
		diff = abs(board[i][j] - board[i][j + 1])
		if diff == 0:
			count += 1
		elif diff == 1:
			# uphill
			if board[i][j] < board[i][j + 1]:
				# condition 4. it's too short to place a slope way
				if count < l:
					flag = False
				else:
					count = 1
			# downhill
			else:
				if count >= 0:
					count = -l + 1
				else:
					flag = False
		# condition 2. the difference is greater than 1
		else:
			flag = False
		j += 1
	if count >= 0 and flag:
		answer += 1
	
	# vertical traverse
	j, count = 0, 1
	flag = True
	while j + 1 < n:
		diff = abs(board2[i][j] - board2[i][j + 1])
		if diff == 0:
			count += 1
		elif diff == 1:
			# uphill
			if board2[i][j] < board2[i][j + 1]:
				# condition 4. it's too short to place a slope way
				if count < l:
					flag = False
				else:
					count = 1
			# downhill
			else:
				if count >= 0:
					count = -l + 1
				else:
					flag = False
		# condition 2. the difference is greater than 1
		else:
			flag = False
		j += 1
	if count >= 0 and flag:
		answer += 1
print(answer)
