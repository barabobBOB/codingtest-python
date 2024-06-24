import sys
input = sys.stdin.readline

N, K = map(int, input().split())
grade = list(map(int, input().split()))

for _ in range(K):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A - 1, B):
        cnt += grade[i]
    avg = cnt/(B-A+1)
    
    print('{:.2f}'.format(round(avg,2)))