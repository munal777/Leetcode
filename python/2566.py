class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        first = 9
        for i in range(len(num)):
            if num[0] != 9:
                first = num[0]
            if num[i] == first:
                num[i] = 9

        return num

