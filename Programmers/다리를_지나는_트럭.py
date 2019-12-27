from collections import deque


def solution(bridge_length, weight_limit, truck_weights):
	answer = 0
	waiting = deque(truck_weights)
	passing = deque()
	
	bridge_weight = 0
	while waiting or passing:
		
		# count time for the trucks on the bridge
		for i in range(len(passing)):
			passing[i][1] -= 1
		
		# if the first truck on the bridge is about to pass
		if passing and passing[0][1] == 0:
			weight, _ = passing.popleft()
			bridge_weight -= weight
		
		# if there's any waiting truck
		if waiting:
			# if the bridge is available
			if len(passing) < bridge_length and bridge_weight + waiting[0] <= weight_limit:
				weight = waiting.popleft()
				passing.append([weight, bridge_length])
				bridge_weight += weight
		answer += 1
		
	return answer


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
