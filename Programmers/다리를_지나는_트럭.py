from collections import deque


def solution(bridge_length, weight, truck_weights):
	answer = 0
	
	passing = deque()
	truck_weights = deque([[w, bridge_length] for w in truck_weights])
	total_weight = 0
	
	while passing or truck_weights:
		answer += 1
		
		# put truck on the bridge
		if truck_weights and total_weight + truck_weights[0][0] < weight:
			truck = truck_weights.popleft()
			total_weight += truck[0]
			passing.append(truck)
			continue
		
		length = len(passing)
		for i in range(length):
			truck = passing.popleft()
			truck[1] -= 1
			if truck[1] > 0:
				passing.append(truck)
			else:
				total_weight -= truck[0]
				
		print(answer, passing, truck_weights)
			
	return answer


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
