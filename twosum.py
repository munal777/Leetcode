def twoSum(nums, target):
    # l = 0
    # r = len(nums) - 1

    # while l < r:
    #     sumed = nums[l] + nums[r]

    #     if sumed == target:
    #         return [l,r]
    #     elif sumed > r:
    #         r -= 1
    #     elif sumed < l:
    #         l += 1
    # for i in range(len(nums)-1):
    #     for j in range(len(nums)-1, i, -1):
    #         sumed = nums[i] + nums[j]
    #         if sumed == target:
    #             return [i,j]
    #         elif sumed < target:
    #             break

    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i  # Store index of current number
    
    return []

nums = [1,2,7,11,22]
target = 3
print(twoSum(nums, target))