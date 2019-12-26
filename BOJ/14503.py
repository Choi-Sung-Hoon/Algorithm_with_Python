import sys

inputLine = sys.stdin.readline().split()
n, m = int(inputLine[0]), int(inputLine[1])
matrix = [[0 for c in range(m)] for r in range(n)]
inputLine = sys.stdin.readline().split()
robot_r, robot_c, robot_dir = int(inputLine[0]), int(inputLine[1]), int(inputLine[2])
for r in range(n):
	inputLine = sys.stdin.readline().split()
	for c in range(m):
		matrix[r][c] = int(inputLine[c])

		
def isInBound(r, c):
	if 0 <= r < n and 0 <= c < m:
		return True
	return False


direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
count = 0
while True:
	# 1. clean the space
	matrix[robot_r][robot_c] = 2
	count += 1
	
	nextDir = robot_dir
	while True:
		# 2. traverse turning to left
		nextDir = (nextDir + 3) % 4
		nextR = robot_r + direction[nextDir][0]
		nextC = robot_c + direction[nextDir][1]
		
		# 2-1 the room is not cleaned yet
		if isInBound(nextR, nextC):
			if matrix[nextR][nextC] == 0:
				robot_r = nextR
				robot_c = nextC
				robot_dir = nextDir
				# go to 1
				break
		
		# the rooms in all directions are traversed and weren't cleaned
		if nextDir == robot_dir:
			nextR = robot_r - direction[robot_dir][0]
			nextC = robot_c - direction[robot_dir][1]
			
			# 2-4 not able to move backward. finish
			if matrix[nextR][nextC] == 1:
				print(count)
				exit()
			# 2-3 move backward
			else:
				robot_r = nextR
				robot_c = nextC
				continue
