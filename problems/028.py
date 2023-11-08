class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        # If needle not in haystack, return -1
        if needle not in haystack:
            return -1

        # Now find the first occurrence
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle:
                return i

        return -1

        return -1