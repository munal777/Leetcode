class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = 0
        r = len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l+1,r+1]
            elif curr_sum > target:
                r -= 1
            else:
                l += 1
        
        return []
    
    # Time Complexity
    # Outer loop → O(n)
    # Binary search → O(log n)
    # O(n log n)

    # def twoSum(self, numbers, target):
    #     for i in range(len(numbers)):
    #         left = i + 1
    #         right = len(numbers) - 1
    #         complement = target - numbers[i]

    #         while left <= right:
    #             mid = (left + right) // 2

    #             if numbers[mid] == complement:
    #                 return [i + 1, mid + 1]
    #             elif numbers[mid] < complement:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1

    #     return []
    

numbers = [2,7,11,15]
target = 9

obj = Solution()
print(obj.twoSum(numbers, target))