class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        for i in range(0,len(nums) - 2,3):
            curr_diff = nums[i+2] - nums[i]

            if curr_diff > k:
                return []
            ans.append([nums[i], nums[i+1], nums[i+2]])
        
        return ans
    

obj = Solution()
# nums = [1,3,4,8,7,9,3,5,1]
# k = 2
nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11]
k = 14
print(obj.divideArray(nums, k))