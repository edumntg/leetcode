class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return
        
        if m == 0:
            nums1[:n] = nums2
            return

        nums1_copy = [x for x in nums1]
        
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            n1 = nums1_copy[i]
            n2 = nums2[j]
            if n1 <= n2:
                i += 1
            else:
                nums1[k+1:] = nums1[k:-1]
                nums1[k] = n2
                j += 1
            
            k += 1

        if j < n:
            for _ in range(n-j):
                nums1[k] = nums2[j]
                j += 1
                k += 1
        
