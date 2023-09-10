n = int(input())
A = []

for _ in range(n):
    A.append(int(input()))

stack = []
num = 1
answer = ""
result = True

for i in range(n):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop()
        if n > su:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)