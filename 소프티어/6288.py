import sys

input = sys.stdin.readline

W, N = map(int, input().split())

recode = []

for _ in range(int(N)):
    # 총 금속의 무게, 1kg당 가격
    M, P = input().split()
    recode.append([int(M), int(P)])

recode.sort(key=lambda x: -x[1])

cnt_price = 0
cnt_kg = 0

while cnt_kg < W:
    for r in recode:
        left_w = W - cnt_kg
        if r[0] == 0:
            continue
            
        if r[0] <= left_w:
            cnt_price += (r[1]*r[0])
            cnt_kg += r[0]
            r[0] = 0

        if r[0] > left_w:
            w = left_w
            cnt_price += (w * r[1])
            cnt_kg += w
            r[1] -= w

print(cnt_price)