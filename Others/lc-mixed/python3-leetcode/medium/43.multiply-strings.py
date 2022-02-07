#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        num1 = [int(x) for x in num1]
        num2 = [int(x) for x in num2]
        num1.reverse()
        num2.reverse()

        result = [0] * (len(num1) + len(num2) - 1)

        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i + j] += num1[i] * num2[j]
        carry = 0
        for i in range(len(result)):
            result[i] += carry
            carry = result[i] // 10
            result[i] %= 10
        if carry:
            result.append(carry)
        return ''.join(reversed([str(x) for x in result]))


# @lc code=end
