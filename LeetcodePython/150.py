class Solution:
    def resolves(self, a, b, Operator):
        if Operator == '+':
            return a + b
        elif Operator == '-':
            return a - b
        elif Operator == '*':
            return a * b
        return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+','-','*','/']
        for i in tokens:
            if i in ops:
                b = stack.pop()
                a = stack.pop()
                ans = self.resolves(a, b, i)
                stack.append(ans)
            else:
                stack.append(int(i))
        return stack.pop()
