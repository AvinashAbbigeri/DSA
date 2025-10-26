# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        i = 0
        j = n - 1
        while j > i:
            sums = numbers[i] + numbers[j]
            if sums == target:
                return [i + 1, j + 1]
            elif sums > target:
                j -= 1
            else:
                i += 1
        