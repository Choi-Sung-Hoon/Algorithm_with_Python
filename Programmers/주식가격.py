def solution(prices):
	answer = [0 for _ in range(len(prices))]
	length = len(prices)
	
	# for all stock prices
	for i, p in enumerate(prices):
		
		# estimate duration
		duration = 0
		for j in range(i + 1, length, 1):
			# count time unconditionally
			duration += 1
			# if a stock price drops
			if prices[j] < p:
				break
		
		answer[i] = duration
		
	return answer


print(solution([1, 2, 3, 2, 3]))
print(solution([498, 501, 470, 489]))
