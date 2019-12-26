import sys

n = int(sys.stdin.readline())
board = [[0 for c in range(n + 1)] for r in range(n + 1)]
for r in range(1, n + 1, 1):
	line = list(map(int, sys.stdin.readline().split()))
	for c in range(1, n + 1, 1):
		board[r][c] = line[c - 1]

team_start = list()
team_link = list()
answer = sys.maxsize


def solution(idx, n):
	if idx == n + 1:
		
		# now we have full teams
		if len(team_start) == len(team_link) == n / 2:
			global answer
			sum_start, sum_link = 0, 0
			
			# get total power of each team with the combination of each team
			for i in range(n // 2):
				for j in range(i + 1, n // 2, 1):
					player1, player2 = team_start[i], team_start[j]
					sum_start += board[player1][player2] + board[player2][player1]
					
					player1, player2 = team_link[i], team_link[j]
					sum_link += board[player1][player2] + board[player2][player1]
			answer = min(answer, abs(sum_start - sum_link))
		return
	
	# push i-th player to start team
	team_start.append(idx)
	solution(idx + 1, n)
	# backtracking
	team_start.pop()

	# push i-th player to link team
	team_link.append(idx)
	solution(idx + 1, n)
	# backtracking
	team_link.pop()


solution(1, n)
print(answer)
