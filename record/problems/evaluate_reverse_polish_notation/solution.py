class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(a, b, op):
            if op == '+': return a+b
            if op == '-': return a-b
            if op == '*': return a*b
            if op == '/': return int(a/b)
        stack = []
        for item in tokens:
            if item in "+-*/":
                b = stack.pop()
                a = stack.pop()
                ans = operation(a,b, item)
                stack.append(ans)
            else:
                stack.append(int(item))
        return stack.pop()
            