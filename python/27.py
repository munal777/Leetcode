def remove_element(nums, k):
    nums.sort()

    l = 0

    while l < len(nums):
        if nums[l] == k:
            nums.pop(l)
        else: 
            l += 1
    
    return len(nums)

nums = [1,1,2,3,4,5,2,2]
k = 2
print(remove_element(nums, k))
