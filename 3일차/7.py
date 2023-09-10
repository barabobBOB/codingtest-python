n = int(input())
m = int(input())

n_list = list(map(int, input().split()))

n_list.sort()

cut = 0
start_index = 0
end_index = n - 1

while start_index < end_index:
    if n_list[start_index] + n_list[end_index] > m:
        end_index -= 1
    elif n_list[start_index] + n_list[end_index] < m:
        start_index += 1
    else:
        cut += 1
        start_index += 1
        end_index -= 1
        

print(cut)