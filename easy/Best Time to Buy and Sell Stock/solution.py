class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 10**4 + 1
        max_profit = 0

        for i in range(0, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

        # Time complexity: O(n)
        # Space complexity: O(1)
