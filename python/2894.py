# 2894. Divisible and Non-divisible Sums Difference

class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        divisible_sum = 0
        non_divisible_sum = 0

        for num in range(1,n+1):
            if num%m == 0:
                divisible_sum += num
            else:
                non_divisible_sum += num