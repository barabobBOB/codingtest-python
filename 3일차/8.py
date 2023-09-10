n = int(input())
n_list = list(map(int, input().split()))

n_list.sort()

cut = 0

for k in range(n):
    find = n_list[k]
    i = 0
    j = n - 1
    while i < j:
        if n_list[i] + n_list[j] == find:
            if i != k and j != k:
               cut += 1
               break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif n_list[i] + n_list[j] < find:
            i += 1
        else:
            j -= 1

print(cut)