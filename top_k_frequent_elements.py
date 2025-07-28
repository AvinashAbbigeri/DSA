class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Counts the frequency of each element in nums
        topk_map = Counter(nums)
        # Takes the ma items and the second element of the tuple and sorts them in descending order
        sorted_items = sorted(topk_map.items(), key = lambda x: x[1], reverse=True)
        # Extracts the top k elements based on frequency
        result = [item[0] for item in sorted_items[:k]]
        return result        