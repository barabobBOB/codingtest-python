import sys
input = sys.stdin.readline

N, K = map(int, input().split())
grade = list(map(int, input().split()))

for i in range(1, len(grade)):
    grade[i] += grade[i-1]

for _ in range(K):
    A, B = map(int, input().split())
    
    if A == 1:
        avg = grade[B-1]/(B-A+1)
    else:
        sum_grade = grade[B-1] - grade[A-2]
        avg = sum_grade/(B-A+1)
    
    print('{:.2f}'.format(round(avg,2)))