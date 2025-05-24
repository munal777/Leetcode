# 2942. Find words containing character
class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        index_list = []

        for word in range(len(words)):
            if x in words[word]:
                index_list.append(word)
        
        return index_list