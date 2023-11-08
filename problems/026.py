class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[current] = nums[i+1]
                current += 1

        return current
