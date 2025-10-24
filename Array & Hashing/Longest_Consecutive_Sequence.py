# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        nums = sorted(set(nums))
        result = 1
        temp = 1
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                temp += 1
                result = max(result, temp)
            else:
                temp = 1
        return result