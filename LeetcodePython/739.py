class Solution:
    def dailyTemperatures(self, temps):
        ans = [0] * len(temps)
        stack = []
        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        return ans
