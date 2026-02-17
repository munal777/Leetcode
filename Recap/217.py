class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hashmap = {}

        for index in range(0, len(nums)):
            curr_num = nums[index] 
            if curr_num in hashmap:
                return True
            hashmap[curr_num] = index
        
        return False
    
nums = [1,2,3,4]
obj = Solution()
print(obj.containsDuplicate(nums))