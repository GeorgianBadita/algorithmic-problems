#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def find_combinations(self, digits, mapping, curr_sol, sols):
        if len(curr_sol) == len(digits):
            sols.append(''.join([x for x in curr_sol]))
            return

        for candidate in mapping[digits[len(curr_sol)]]:
            if len(curr_sol) < len(digits):
                curr_sol.append(candidate)
                self.find_combinations(digits, mapping, curr_sol, sols)
                curr_sol.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        sols = []
        self.find_combinations(digits, mapping, [], sols)
        return sols


# @lc code=end
