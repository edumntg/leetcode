class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 1:
            return strs[0]

        # First, we sort the array of strings by the length of words in ascending order
        sorted(strs, key = len)

        # Loop through the characters in the shortest word
        longest = ''
        for i in range(len(strs[0])+1):
            prefix = strs[0][:i]
            print(prefix)
            if all([word.startswith(prefix) for word in strs]):
                longest = prefix

        return longest