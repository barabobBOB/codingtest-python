from math import remainder


n, m = map(int, input().split())
nums = list(map(int, input().split()))

cut = 0

prefix_nums = [0] * n
C = [0] * m

prefix_nums[0] = nums[0]

for i in range(1, n):
    prefix_nums[i] = prefix_nums[i - 1] + nums[i]


for i in range(n):
    remainder = prefix_nums[i] % m
    if remainder == 0:
        cut += 1
    C[remainder] += 1

for i in range(m):
    if C[i]>1:
        cut += (C[i]*(C[i]-1) // 2)
    

print(cut)