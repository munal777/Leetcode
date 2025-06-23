class Solution:

    def removeDuplicate(self, nums):

        l = 0

        while l < len(nums)-1:
            if nums[l] == nums[l + 1]:
                nums.pop(l+1)
            else:
                l += 1
        
        return nums

# nums = [1,2,2,3,4,4,5]
nums = [1,1,2]
obj = Solution()
print(obj.removeDuplicate(nums))             