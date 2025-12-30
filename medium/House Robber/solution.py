class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Say dp[i] is the max amount of money can rob
        # up to house at index i.
        # At every house, you choose either to rob it
        # or to skip it. So dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        n = len(nums)
        dp = [0] * n
        # base cases:
        dp[0] = nums[0]
        if n == 1:
            return dp[n - 1]
        dp[1] = max(dp[0], nums[1])
        if n <= 2:
            return dp[n - 1]

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]
