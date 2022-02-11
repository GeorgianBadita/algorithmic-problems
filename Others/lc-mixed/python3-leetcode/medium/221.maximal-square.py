#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        max_dp = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    dp[row][col] = 1
                    max_dp = 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if dp[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i]
                                       [j - 1], dp[i - 1][j - 1])
                max_dp = max(max_dp, dp[i][j])
        return max_dp ** 2

# @lc code=end
