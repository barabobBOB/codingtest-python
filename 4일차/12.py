N = int(input())

a = list(map(int, input().split()))
stack = []
answer = [0] * N

for i in range(N):
    while stack and a[stack[-1]] < a[i]:
        answer[stack.pop()] = a[i]
    stack.append(i)

while stack:
    answer[stack.pop()] = -1

print(' '.join(map(str, answer)))