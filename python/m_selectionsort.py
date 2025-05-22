def selectionSort(nums):

    n = len(nums)
    for i in range(n-1):
        min_length = i
        for j in range(i+1, n):
            if len(nums[j]) < len(nums[min_length]):
                min_length = j
            
        nums[i], nums[min_length] = nums[min_length], nums[i]

    return nums

nums = ["apple", "bat", "a", "banana"]
print(selectionSort(nums))


