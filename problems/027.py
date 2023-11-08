class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        current = 0
        n = 0
        while nums.count(val) > 0:
            if nums[current] == val:
                # Move the elements starting at i+1 one space to the left
                nums[current:] = nums[current+1:] + [None]*(current+1)
                n += current + 1
            else:
                current += 1
        
        return len(nums) - n