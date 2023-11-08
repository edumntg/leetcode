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

        # Initialize carry with the value we are adding
        carry = 1

        # Index of the number we are adding 1
        index = n-1

        # Helper variable
        done = False
        while carry != 0 and index >= 0:
            val = digits[index] + carry # Add carry
            carry = 0 # Now we are not carrying anything

            if val == 10: # We must carry 1 again
                val = 0
                carry = 1
            else:
                done = True

            digits[index] = val # Update number

            if done: # We are not carrying anything so no need to check other digits
                break
            
            index -= 1 # Move one index to the left

        # If at the end we still carry 1, it means the higher digit was a 9
        if carry == 1:
            digits = [1] + digits

        return digits