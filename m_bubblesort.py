class Bubblesort:
    """
    Given an array of integers nums, sort the array in ascending order using the Bubble
    Sort algorithm. Additionally, return the total number of swaps performed during
    the sorting process.
    """
    def bubblesort(self, nums, k):
        n = 0
        for i in range(len(nums)):
            sweped = False
            # for j in range(len(nums) - 1 - i):
            mins = min(len(nums) - 1, k + i)
            for j in range(mins):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    n += 1
                    sweped = True
            
            if not sweped:
                break
        
        return (nums,n)

nums = [1, 2, 5, 3, 8, 4] 
obj = Bubblesort()
print(obj.bubblesort(nums, 2))
