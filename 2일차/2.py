n = int(input())
numbers = list(map(int, input().split()))

max_score = max(numbers)
sum_score = sum(numbers)

print(sum_score * 100/max_score/n)