class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ass in asteroids:
            while stack and stack[-1]  > 0 and ass < 0:
                if abs(ass) > stack[-1]:
                    stack.pop()
                    continue

                if abs(ass) == stack[-1]:
                    stack.pop()
                    break
                else:
                    break

            else:
                stack.append(ass)

        return stack