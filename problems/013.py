class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Declare the values of each roman numeral
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # We specify the substraction cases
        substraction = {
            'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M']
        }

        roman_value = 0

        # Convert the roman string to list
        roman_lst = list(s)

        while len(roman_lst) > 0:
            if len(roman_lst) == 1:
                roman_value += values[roman_lst[0]]
                break

            # Get first and second numerals
            X1 = roman_lst[0]
            X2 = roman_lst[1]

            # Get their values
            x1 = values[X1]
            x2 = values[X2]

            # Check if x1 must be subtracted from x2
            if X1 in substraction and X2 in substraction[X1]:
                roman_value += x2 - x1
                roman_lst.pop(0)
                roman_lst.pop(0)
            else:
                # Just add X1
                roman_value += x1
                roman_lst.pop(0)
        return roman_value


        