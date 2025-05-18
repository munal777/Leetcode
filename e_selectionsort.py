def selectionSort(nums):
    n = len(nums)
    
    for i in range(n-1):
        min_num = i
        for j in range(i+1, n):
            if nums[j][1] < nums[min_num][1]:
                min_num = j

        nums[i], nums[min_num] = nums[min_num], nums[i] 

    return nums

arr = [64, 25, 12, 22, 11]
k = 3
nums = [(3, 2), (1, 5), (4, 1), (2, 3)] 

print(selectionSort(nums))























