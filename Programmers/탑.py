def solution(heights):
	answer = []
	
	for i, height in enumerate(heights):
		found = False
		# for all front towers from the nearest tower
		for j in range(i - 1, -1, -1):
			if heights[j] > height:
				answer.append(j + 1)
				found = True
				break
		# if there's no higher tower
		if not found:
			answer.append(0)
	
	return answer


print(solution([6,9,5,7,4]))
print(solution([3,9,9,3,5,7,2]))
print(solution([1,5,3,6,7,6,5]))
