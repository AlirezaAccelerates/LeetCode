class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        j = 0
        for i in range(len(list(haystack))):
            if list(haystack)[i:i+len(list(needle))] == list(needle):
                j = 1
                return i
                break
        if j == 0:
            return -1
            
        