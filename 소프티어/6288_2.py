import sys

input = sys.stdin.readline

W, N = map(int, input().split())

recode = [list(map(int,input().split())) for _ in range(N)]
recode.sort(key=lambda x: -x[1])
cnt_price = 0

for m, p in recode:
    # 담을 수 있는 최대치 무게를 가지고 있을 때
    if m <= W:
        cnt_price += m * p
        W -= m

    elif m > W:
        cnt_price += W * p
        W = 0
        
print(cnt_price)