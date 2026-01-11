class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        actual_sum = sum(nums)
        sum_if_not_missing = (n + 1) * (0 + n) / 2
        return sum_if_not_missing - actual_sum
