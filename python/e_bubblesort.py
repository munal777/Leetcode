class bubblesort:
    """
    bubble sort algorithm is the n^2 time complexity
    """
    def bubblesort(self, nums):
        for i in range(len(nums) - 1):
            swap = False
            for j in range(len(nums) -1 -i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j] 
                    swap = True
                
            if not swap:
                break
        return nums



nums = [1, 2, 5, 3, 8, 4] 
obj = bubblesort()
print(obj.bubblesort(nums))

