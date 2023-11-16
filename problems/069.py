class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        # Base cases
        if x <= 1:
            return x
        
        # I use the Heron's method
        # Chose the middle value between 1 and x
        x0 = (1.0 + x) / 2.0

        # Declare an epsilon of 0.1 (should be enough since the solution must be rounded to integer)
        eps = 0.1

        # Initial error
        err = 1E9

        # Execute algorithm while error is higher than epsilon
        while err > eps:
            # Compute new guess
            xsol = (x0 + x / x0) / 2.0

            # Calculate new error
            err = abs(x - xsol*xsol)

            # Update previous sol
            x0 = xsol
        
        # Now, round down to nearest integer
        return int(xsol)