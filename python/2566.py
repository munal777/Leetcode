class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = list(str(num)) 

        if num_str[0] != '9':
            first = num_str[0]
            for i in range(len(num_str)):
                if num_str[i] == first:
                    num_str[i] = '9'  

        new_num = int(''.join(num_str))

        return new_num

obj = Solution()
num = 11891
print(obj.minMaxDifference(num))