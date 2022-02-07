#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = [x for x in path.split('/') if x != '']
        current_paths = []
        for path in paths:
            if path == ".":
                continue
            if path == "..":
                if current_paths:
                    current_paths.pop()
            else:
                current_paths.append(path)

        return '/' if not current_paths else '/'.join([''] + current_paths)
# @lc code=end
