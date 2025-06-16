class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_diff = -1
        for i in range(len(nums)-1):    
            curr_diff = nums[i+1] - nums[i]
            if curr_diff > max_diff:
                max_diff = curr_diff

        last_max = nums[len(nums)-1] - nums[0]

        if max_diff < last_max:
            max_diff = last_max

        return max_diff

obj = Solution()
# nums = [1,5,2,10]
nums = [8,33,55,68,65,41,63]
print(obj.maximumDifference(nums))