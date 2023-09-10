import sys

n = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
num = 1
answer = []
result = True

for i in range(n):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer.append("+")
        stack.pop()
        answer.append("-")
    else:
        n = stack.pop()
        if n > su:
            print("NO")
            result = False
            break
        else:
            answer.append("-")

if result:
    print("\n".join(answer))
