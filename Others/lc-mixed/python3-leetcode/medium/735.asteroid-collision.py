from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                if stack and stack[-1] < 0:
                    last = stack.pop()
                    if abs(last) > asteroid:
                        stack.append(last)
                    elif abs(last) < asteroid:
                        stack.append(asteroid)
                elif not stack or stack[-1] > 0:
                    stack.append(asteroid)
            else:
                if stack and stack[-1] > 0:
                    last = stack.pop()
                    if last > abs(asteroid):
                        stack.append(last)
                    elif last < abs(asteroid):
                        stack.append(asteroid)
                elif not stack or stack[-1] < 0:
                    stack.append(asteroid)
        return stack


print(Solution().asteroidCollision(
    [-5, -5, 10]))
