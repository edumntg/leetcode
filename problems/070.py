class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        def recur(n):
            if n <= 2:
                return n
            
            ways = [0]*(n+1)
            ways[1] = 1
            ways[2] = 2

            # Now calculatethe rest ones as ways[i] = ways[i-1] + ways[i-2]
            for i in range(3, n+1):
                ways[i] = ways[i-1] + ways[i-2]
            
            return ways[n]
        
        return recur(n)