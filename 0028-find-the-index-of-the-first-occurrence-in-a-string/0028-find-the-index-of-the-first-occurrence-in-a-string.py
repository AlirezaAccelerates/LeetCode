class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h_words = list(haystack)
        n_words = list(needle)
        j = 0
        for i in range(len(h_words)):
            if h_words[i:i+len(n_words)] == n_words:
                j = 1
                return i
                break
        if j == 0:
            return -1
            
        