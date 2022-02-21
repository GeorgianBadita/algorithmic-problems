#
# @lc app=leetcode id=51 lang=python3
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

    def backtrack_queens(self, n, used, sol, sols):
        for col in range(n):
            if not used[col] and self.is_consistent(sol, col):
                used[col] = True
                sol.append(col)
                if len(sol) == n:
                    sols.append(sol[:])
                self.backtrack_queens(n, used, sol, sols)
                used[col] = False
                sol.pop()

    def solveNQueens(self, n: int) -> List[List[str]]:
        sols = []
        self.backtrack_queens(n, [False]*n, [], sols)
        boards = [[['.']*n for _ in range(n)] for _ in range(len(sols))]
        for idx, curr_sol in enumerate(sols):
            for row, col in enumerate(curr_sol):
                boards[idx][row][col] = 'Q'
            for row in range(len(curr_sol)):
                boards[idx][row] = ''.join(boards[idx][row])
        return boards

# @lc code=end
