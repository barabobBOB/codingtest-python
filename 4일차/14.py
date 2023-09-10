from queue import PriorityQueue

n = int(input())
a = PriorityQueue()

for i in range(n):
    request = int(input())
    if request == 0:
        if a.empty():
            print('0')
        else:
            temp = a.get()
            print(str(temp[1]))
    else:
        a.put(abs(request), request)