nums = list(map(int, input()))
    
for i in range(len(nums)):
    max = i
    for j in range(i+1, len(nums)):
        if nums[max] < nums[j]:
            max = j
    if nums[max] > nums[i]:
        temp = nums[i]
        nums[i] = nums[max]
        nums[max] = temp

result = ''

for i in nums:
    result += str(i)
    
print(result)