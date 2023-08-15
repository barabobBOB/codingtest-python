n, m = map(int, input().split())

numbers_list = [[0] * (n + 1)]
prefix_list = [[0] * (n + 1) for _ in range(n+1)]

for _ in range(n):
    numbers_list.append([0] + list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_list[i][j] = prefix_list[i][j-1] + prefix_list[i-1][j] - prefix_list[i-1][j-1] + numbers_list[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix_list[x2][y2] - prefix_list[x1 - 1][y2] - prefix_list[x2][y1 - 1] + prefix_list[x1 - 1][y1 - 1])