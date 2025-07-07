# two sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums) - 1

        l = 0
        r = n

        while l < r:
            sums = nums[l] + nums[r]

            if sums == target:
                return [l,r]
            elif (l + 1) == r:
                l += 1
                r = n
            else:
                r -= 1



obj = Solution()
# nums = [2,7,11,15] 
# target = 9
# nums = [3,2,4]
# target = 6
nums = [3,3]
target = 6
print(obj.twoSum(nums, target))