from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
street = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for r in range(N):
  for c in range(N):
    if street[r][c] == 1:
        house.append([r, c])
    elif street[r][c] == 2:
        chicken.append([r, c])

result = 1e9
for x in combinations(chicken, M):
    graph_dist = 0
    for h in house:
        house_dist = 1e9
        for k in x:
            house_dist = min(house_dist, abs(h[0]-k[0]) + abs(h[1]-k[1]))
        graph_dist += house_dist
    result = min(result, graph_dist)

print(result)
