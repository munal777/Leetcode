class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
    

        if n < 2:
            return 0
        sieve = [True] * n
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5)+1):
            if sieve[i]:
                for j in range(i*i, n, i):
                    sieve[j] = False
        return sum(sieve)

    #     total_prime = 0

    #     for i in range(2,n):
    #         if self.check_prime(i):
    #             total_prime += 1

    #     return total_prime
                
    # def check_prime(self,n):
        # if n < 2:
        #         return False
    #     for i in range(2,int(n**0.5)+1):
    #         if n%i == 0:
    #             return False
    #     return True
    

    

# obj = Solution()
# print(obj.countPrimes(2))


sieve = [True] * 10

print(sieve)