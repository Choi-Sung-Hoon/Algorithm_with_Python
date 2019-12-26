import sys

n = int(sys.stdin.readline())
time = [0 for _ in range(n)]
price = [0 for _ in range(n)]
dp = [0 for _ in range(n + 1)]
for i in range(n):
	time[i], price[i] = map(int, sys.stdin.readline().split())
	
for i in range(n):
	# if sum of the price of today is greater than sum of the price of tomorrow, update the maximum price
	dp[i + 1] = max(dp[i], dp[i + 1])
	
	# if i start to work from today, it will end after time[i] days
	if i + time[i] <= n:
		# compare the current maximum price after time[i] days with the maximum sum of today
		dp[i + time[i]] = max(dp[i + time[i]], dp[i] + price[i])
print(dp[n])
