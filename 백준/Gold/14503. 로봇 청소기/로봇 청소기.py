import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# d = 0, 북 / 1, 동 / 2, 남 / 3, 서
r, c, d = map(int, input().split())
# 1이면 벽
# 청소가 완료된 칸은 2
clean = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0

while True:
    if clean[r][c] == 0:
        clean[r][c] = 2
        cnt += 1
    
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if not clean[r + 1][c] == 0 and not clean[r][c+1] == 0 and not clean[r - 1][c] == 0 and not clean[r][c - 1] == 0:
        nx, ny = 0, 0
        # 후진
        # 남 -> 북
        if d + 2 == 4:
            nx, ny = r + dx[0], c + dy[0]
        # 서 -> 동
        elif d + 2 == 5:
            nx, ny = r + dx[1], c + dy[1]
        else:
            nx, ny = r + dx[d + 2], c + dy[d + 2]
        if clean[nx][ny] == 1:
            break
        if clean[nx][ny] == 2:
            r, c = nx, ny
    else:
        for _ in range(4):
            nx, ny = 0, 0
            if d - 1 == -1:
                d = 3
            else:
                d -= 1
            nx, ny = r + dx[d], c + dy[d]
            if clean[nx][ny] == 0:
                r, c = nx, ny
                clean[nx][ny] = 2
                cnt += 1
                break

print(cnt)