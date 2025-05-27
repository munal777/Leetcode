# 2131. Longest Palindrome by Concatenating Two Letter Words

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        words_dict = {}

        for word in words:
            if word not in words_dict: 
                words_dict[word] = 1
            else:
                words_dict[word] += 1
        
        return words_dict

obj = Solution()

# print(obj.longestPalindrome(["lc","cl","gg"]))
print(obj.longestPalindrome(["ab","ty","yt","lc","cl","ab"]))