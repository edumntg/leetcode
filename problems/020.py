class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # List to act as stack
        stack = []

        closing = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        opening = {val: key for key, val in closing.items()}

        # Convert to string to list
        s_lst = list(s)
        while s_lst:
            bracket = s_lst.pop(0)
            if bracket in ')]}': # it is a closing bracket
                # Check if its corresponding opening bracket is at the top of the stack
                if len(stack) == 0:
                    return False

                if opening[bracket] != stack[-1]:
                    return False

                # Remove the corresponding opening bracket from the stack
                stack.pop(-1)
            else: # It is an opening bracket
                stack.append(bracket)

        return len(stack) == 0 # Return true if the stack is empty