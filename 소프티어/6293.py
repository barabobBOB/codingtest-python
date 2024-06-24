import sys

input = sys.stdin.readline

N = int(input())
stone_w = list(map(int, input().split()))

# 마지막으로 밟고 가는 돌일 때 최대 몇번?
dp = [1] * N

for i in range(N):
    cnt = 0
    for j in range(i):
        if stone_w[j] < stone_w[i]:
            cnt = max(dp[j], cnt)
    # 해당 돌 횟수까지
    dp[i] = cnt + 1
    
print(max(dp))