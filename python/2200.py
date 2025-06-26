class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """

        result = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] == key and abs(i-j) <= k:
                    result.append(i)
                    break

        return result


obj = Solution()
nums = [3,4,9,1,3,9,5]
key = 9
k = 1
# nums = [2,2,2,2,2]
# key = 2
# k = 2
print(obj.findKDistantIndices(nums, key, k))