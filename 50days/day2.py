class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        n = len(nums) - 1
        while l < n:
            if nums[l] == nums[l+1]:
                nums.pop(l+1)
                n = len(nums) - 1
            else:
                l += 1
        
        return len(nums)


obj = Solution()
# nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
print(obj.removeDuplicates(nums))