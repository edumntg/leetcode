class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Base case: target is in the array
        if target in nums:
            return nums.index(target)

        # Find the index where it should be inserted
        for i in range(len(nums)):
            if target <= nums[i]:
                return i

        return len(nums)

        