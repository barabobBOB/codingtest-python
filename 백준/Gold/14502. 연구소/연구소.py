from collections import deque
from itertools import combinations

import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]

result = 0

# 0은 빈 칸, 1은 벽, 2는 바이러스

# 빈칸 찾기와 바이러스 위치 찾기
empty_spots = []
virus_positions = []
for i in range(N):
    for j in range(M):
        if map_list[i][j] == 0:
            empty_spots.append((i, j))
        elif map_list[i][j] == 2:
            virus_positions.append((i, j))

# bfs
def bfs(graph):
    q = deque(virus_positions)
    visited = [[False] * M for _ in range(N)]
    
    for vx, vy in virus_positions:
        visited[vx][vy] = True

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    graph[nx][ny] = 2
                    q.append((nx, ny))

# 안전 영역 체크
def safe_check(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

for spot in combinations(empty_spots, 3):
    graph = [m[:] for m in map_list]
    for x, y in spot:
        graph[x][y] = 1
    bfs(graph)
    cnt = safe_check(graph)
    result = max(cnt, result)

    # 최대 가능한 안전 영역을 찾으면 조기 종료
    if result == len(empty_spots) - 3:
        break
    
# 최댓값 출력
print(result)