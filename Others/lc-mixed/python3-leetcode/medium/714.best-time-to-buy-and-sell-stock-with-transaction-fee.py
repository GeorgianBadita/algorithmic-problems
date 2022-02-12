#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] - prices[i] > fee:
                profit += prices[i + 1] - prices[i] - fee
        return profit
# @lc code=end
