class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # --- O(n2) time complexity approach ---
        # for i in range(0,len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         sums = nums[i] + nums[j]
        #         if sums == target:
        #             return [i,j]

        # return []

        # ---  O(n) time complexity approach ---
        maps = {}

        for index in range(0, len(nums)):
            curr_num = nums[index]
            complement_num = target - curr_num
            if  complement_num in maps:
                return [maps[complement_num], index]
            
            maps[curr_num] = index
        
        return []



nums = [2,7,11,15]
obj = Solution()
print(obj.twoSum(nums, 9))