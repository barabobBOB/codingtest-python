from collections import deque
from itertools import combinations
import copy

import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]

result = 0

# 0은 빈 칸, 1은 벽, 2는 바이러스

# 빈칸 찾기
empty_spot = []
for i in range(N):
    for j in range(M):
        if map_list[i][j] == 0:
            empty_spot.append([i, j])

# bfs
def bfs(i, j, visited, graph):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            # print(nx, ny)
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:
                    continue
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    graph[nx][ny] = 2
                    q.append((nx, ny))
                
    return visited, graph

# 안전 영역 체크
def safe_check(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

for spot in combinations(empty_spot, 3):
    visited = [[False] * M for _ in range(N)]
    graph = copy.deepcopy(map_list)
    for x, y in spot:
        graph[x][y] = 1
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 2:
                visited, graph = bfs(i, j, visited, graph)
    cnt = safe_check(graph)
    result = max(cnt, result)

# 최댓값 출력
print(result)