s, p = map(int, input().split())
text = list(input())

check_list = list(map(int, input().split()))
current_list = [0] * 4


cut = 0
result = 0

def add(str):
    global cut, check_list, current_list
    
    if str == 'A':
        current_list[0] += 1
        if check_list[0] == current_list[0]:
            cut += 1
    if str == 'C':
        current_list[1] += 1
        if check_list[1] == current_list[1]:
            cut += 1
    if str == 'G':
        current_list[2] += 1
        if check_list[2] == current_list[2]:
            cut += 1
    if str == 'T':
        current_list[3] += 1
        if check_list[3] == current_list[3]:
            cut += 1

def remove(str):
    global cut, check_list, current_list
    
    if str == 'A':
        if current_list[0] == check_list[0]:
            cut -= 1
        current_list[0] -= 1
    if str == 'C':
        if current_list[1] == check_list[1]:
            cut -= 1
        current_list[1] -= 1
    if str == 'G':
        if current_list[2] == check_list[2]:
            cut -= 1
        current_list[2] -= 1
    if str == 'T':
        if current_list[3] == check_list[3]:
            cut -= 1
        current_list[3] -= 1

# 0 일 때
for i in range(4):
    if check_list[i] == 0:
        cut += 1

# 초기 4자리     
for i in range(p):
    add(text[i])
    
if cut == 4:
    result+=1

for i in range(p, s):
    j = i - p  
    
    add(text[i])
    remove(text[j])
    
    if cut == 4:
        result+=1
        

    
print(result)