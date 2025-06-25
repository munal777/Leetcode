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
            if nums[i] == key:
                result.append(i)
        
        pre_res = []

        for i in result:
            start = max(0, i-k)
            end = min(len(nums)-1, i+k)

            for i in range(start, end + 1):
                pre_res.append(i)
            
        return sorted(pre_res)



obj = Solution()
nums = [3,4,9,1,3,9,5]
key = 9
k = 1
print(obj.findKDistantIndices(nums, key, k))