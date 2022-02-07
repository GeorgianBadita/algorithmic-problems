#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def cnt_and_say(self, current):
        result = ""
        index = 0
        while index < len(current):
            cnt = 1
            val = current[index]
            while index + 1 < len(current) and current[index] == current[index + 1]:
                index += 1
                cnt += 1
            result += f"{cnt}{val}"
            index += 1
        return result

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        res = "1"
        for _ in range(1, n):
            res = self.cnt_and_say(res)
        return res
# @lc code=end
