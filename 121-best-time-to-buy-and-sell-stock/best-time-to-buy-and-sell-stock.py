class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = sys.maxsize
        max_profit = 0

        for i in range(len(prices)):
            if (prices[i] < min_price):
                min_price = prices[i]
            else:
                profit = prices[i] - min_price
                max_profit = max(max_profit, profit)

        return max_profit  