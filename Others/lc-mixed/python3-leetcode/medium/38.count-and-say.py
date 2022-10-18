class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        if n == 3:
            return '21'

        last = self.countAndSay(n - 1)
        
        curr_dig_cnt = 1
        res = ''
        for idx in range(len(last) - 1):
            if last[idx] != last[idx + 1]:
                res += f'{curr_dig_cnt}{last[idx]}'
                curr_dig_cnt = 1
            else:
                curr_dig_cnt += 1

        res += f'{curr_dig_cnt}{last[-1]}'
        return res
