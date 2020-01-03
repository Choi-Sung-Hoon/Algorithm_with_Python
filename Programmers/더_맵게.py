import heapq


def solution(scoville, K):
	answer = 0
	
	# make scoville list heap
	heapq.heapify(scoville)
	# while minimum of the heap is lower than K
	while scoville[0] < K:
		# mix 2 foods
		a = heapq.heappop(scoville)
		b = heapq.heappop(scoville)
		heapq.heappush(scoville, a + (b * 2))
		answer += 1
		
		if len(scoville) == 1 and scoville[0] < K:
			return -1
		
	return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
