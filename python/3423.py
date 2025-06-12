# 3423. Maximum Difference Between Adjacent Elements in a Circular Array

class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        abs_value  = 0
        l = 0 
        r = len(nums) - 1

        for i in range(len(nums)-1):
            curr_abs = abs(nums[i]- nums[i+1])

            if curr_abs > abs_value:
                abs_value = curr_abs

        circular_value = abs(nums[l] - nums[r])
        if abs_value < circular_value:
            return  circular_value
        return abs_value
    

obj = Solution()
nums = [3,2,-5,-3]
print(obj.maxAdjacentDistance(nums))