class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # [1, 2, 3] = 1*100 + 2*10 + 3*1 = 1*10^2 + 2*10^1 + 3*10^0
        # [4, 3, 2, 1] = 4*1000 + 3*100 + 2*10 + 1 = 4*10^3 + 3*10^2 + 2*10^1 + 1*10^0

        # Get number of digits
        n = len(digits)

        # Compute the real number
        value = sum([x*10**(n-1-i) for i, x in enumerate(digits)])

        # Add 1
        value += 1

        # Convert to string
        value_str = str(value)
        
        # Convert to list
        value_lst = list(value_str)

        # Convert list of ints
        value_int = [int(x) for x in value_lst]

        # Return
        return value_int        