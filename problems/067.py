class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # a = [1, 1]
        # b = [0, 1]

        # Convert strings to list of ints
        a_int = [int(x) for x in a]
        b_int = [int(x) for x in b]

        # Pad the shortest array with zeros at the start
        longest = a_int
        shortest = b_int
        if len(b_int) > len(a_int):
            longest = b_int
            shortest = a_int

        n = len(longest)
        m = len(shortest)

        shortest = [0]*(n-m) + shortest

        # Now, add binary numbers
        result = []
        carry = 0
        index = n - 1
        while len(shortest) > 0:
            b1 = shortest.pop(-1)
            b2 = longest.pop(-1)

            # Add the two digits
            val = b1 + b2 + carry
            carry = 0
            if val == 2:
                val = 0
                carry = 1
            elif val == 3:
                val = 1
                carry = 1
                    
            # Append result
            result = [val] + result
            index -= 1
        
        if carry:
            result = [1] + result

        return ''.join([str(x) for x in result])
            
            

