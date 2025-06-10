# 125. Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        valid_s = ""
        
        for char in s:
            if char.isalpha():
                valid_s += char.lower()
            if char.isnumeric():
                valid_s += char
        return True if valid_s[0:len(valid_s)] == valid_s[::-1] else False