#
# @lc app=leetcode id=52 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def is_consistent(self, sol, new_col):
        if not sol:
            return True
        new_row = len(sol)
        for row in range(len(sol)):
            if abs(row - new_row) == abs(sol[row] - new_col):
                return False
        return True

    def backtrack_queens(self, n, used, sol):
        if len(sol) == n:
            return 1
        result = 0
        for col in range(n):
            if not used[col] and self.is_consistent(sol, col):
                used[col] = True
                sol.append(col)
                result += self.backtrack_queens(n, used, sol)
                used[col] = False
                sol.pop()
        return result

    def totalNQueens(self, n: int) -> List[List[str]]:
        return self.backtrack_queens(n, [False]*n, [])


# @lc code=end
