class BubbleSort:
    def sortAlgorithm(self, nums):
        """
        sort the list in asecnding order on the basis of second element of tuples
        """
        for i in range(len(nums) - 1):
            swaped = False
            for j in range(len(nums) - 1 - i):
                if nums[j][1] > nums[j+1][1]:
                   nums[j], nums[j+1] = nums[j+1], nums[j]
                   swaped = True
                
            if not swaped:
                break

        return nums


arr = [(1, 3), (4, 1), (5, 2), (6, 4)]

obj = BubbleSort()
print(obj.sortAlgorithm(arr))
