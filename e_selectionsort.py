def selectionSort(nums):
    for i in range(len(nums)-1):
        min_num = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min_num]:
                min_num = j
        nums[i], nums[min_num] = nums[min_num], nums[i]

    return nums     

arr = [64, 25, 12, 22, 11]
print(selectionSort(arr))