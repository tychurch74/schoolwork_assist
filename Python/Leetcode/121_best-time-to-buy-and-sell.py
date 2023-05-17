class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mi = prices[0]
        ma = 0
        for i in range(1, len(prices)):
            if prices[i] < mi:
                mi = prices[i]
            else:
                ma = max(ma, prices[i] - mi)
        return ma
