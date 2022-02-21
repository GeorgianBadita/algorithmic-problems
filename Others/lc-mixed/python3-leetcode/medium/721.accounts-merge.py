#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.__father = [x for x in range(n)]

    def union(self, x, y):
        self.__father[self.find(x)] = self.find(y)

    def find(self, x):
        if x != self.__father[x]:
            self.__father[x] = self.find(self.__father[x])
        return self.__father[x]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i

        ans = {}
        for email, owner in ownership.items():
            owner_id = uf.find(owner)
            if owner_id in ans:
                ans[owner_id].append(email)
            else:
                ans[owner_id] = [email]

        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
# @lc code=end
