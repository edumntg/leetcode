class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Create a function to check resursively if a string is palindrome
        def recur(x_str):
            # Base case
            if len(x_str) == 1:
                return True

            # Another case
            if len(x_str) == 2:
                return x_str[0] == x_str[1]
            
            return x_str[0] == x_str[-1] and recur(x_str[1:-1])

        return recur(str(x))