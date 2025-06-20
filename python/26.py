class Solution:

    def removeDuplicate(self, nums):

        l = 0
        r = len(nums) 
        ans = []

        while l < r:
            if nums[l] not in ans:
                ans.append(nums[l])
            l += 1

        return ans


# nums = [1,2,2,3,4,4,5]
nums = [1,1,2]
obj = Solution()
print(obj.removeDuplicate(nums))             