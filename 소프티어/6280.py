import sys
input = sys.stdin.readline 
n = int(input())

dp = [0] * 16
dp[0] = 2

for i in range(1, n+1):
    dp[i] = dp[i - 1] + (2**(i-1))

print(dp[n]**2)