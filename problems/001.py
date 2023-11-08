class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # We want nums[i] + nums[j] = target
        # But also we can calculate target - nums[i]
        # And check if this difference is in the array
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i: # If the difference is in the array, then we find it
                # We need to find the indx of the diff value, but ignoring the index i in case it is the same

                return [i, nums.index(diff)]
        