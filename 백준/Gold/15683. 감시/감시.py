import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# cctv 종류, x 좌표, y 좌표
cctv = []

# 사무실 정보
board = []

#cctv 방향 정보
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]]

for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def fill(board, mode, x, y):
    # CCTV 방향에 따라
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i] 
            ny += dy[i]
            # 범위를 넘어가면 중단
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            # 벽이면 중단 
            if board[nx][ny] == 6:
                break
            # 감시 가능 
            elif board[nx][ny] == 0:
                board[nx][ny] = -1

def dfs(depth, board):
    # 최소값
    global min_value
    
    # 탐색완료
    if depth == len(cctv):
        count = 0
        # 사각지대 찾기
        for i in range(n):
            count += board[i].count(0)
        # 최소값 업데이트
        min_value = min(min_value, count)
        return
    
    temp = [b[:] for b in board]
    
    # 탐색할 cctv
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth + 1, temp)
        temp = [b[:] for b in board]


min_value = 1e9
dfs(0, board)
print(min_value)