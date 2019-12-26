import sys
from copy import deepcopy

inputLine = sys.stdin.readline().split()
n, m = int(inputLine[0]), int(inputLine[1])

matrix = [[0 for c in range(m)] for r in range(n)]
safeSectorList = list()
virusList = list()
for r in range(n):
	inputLine = sys.stdin.readline().split()
	for c in range(m):
		matrix[r][c] = int(inputLine[c])
		
		if matrix[r][c] == 0:
			safeSectorList.append((r, c))
		elif matrix[r][c] == 2:
			virusList.append((r, c))

# brute force for all safe sectors
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
maxCount = 0
length = len(safeSectorList)
for i in range(0, length - 2):
	for j in range(i + 1, length - 1):
		for k in range(j + 1, length):
			# copy matrix
			copy = deepcopy(matrix)
			
			# build new 3 walls
			copy[safeSectorList[i][0]][safeSectorList[i][1]] = 1
			copy[safeSectorList[j][0]][safeSectorList[j][1]] = 1
			copy[safeSectorList[k][0]][safeSectorList[k][1]] = 1
			
			# spread viruses (BFS)
			for virus in virusList:
				queue = [virus]
				visited = set()
				while queue:
					cur_r, cur_c = queue.pop()
					# for 4 directions
					for dr, dc in directions:
						nextR = cur_r + dr
						nextC = cur_c + dc
						# is in boundary
						if 0 <= nextR < n and 0 <= nextC < m:
							# is available to visit
							if copy[nextR][nextC] == 0 and (nextR, nextC) not in visited:
								copy[nextR][nextC] = 2
								queue.append((nextR, nextC))
					visited.add((cur_r, cur_c))
			
			# count safe sectors
			count = 0
			for r in range(n):
				for c in range(m):
					if copy[r][c] == 0:
						count += 1
			if maxCount < count:
				maxCount = count
print(maxCount)
