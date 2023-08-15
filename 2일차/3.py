n, m = map(int, input().split())
numbers = list(map(int, input().split()))

prefix_sum = [0]
temp = 0

for i in numbers:
    temp += i
    prefix_sum.append(temp)
    
for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j]-prefix_sum[i-1])
