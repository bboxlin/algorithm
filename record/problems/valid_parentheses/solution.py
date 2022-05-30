class Solution:
    def isValid(self, s: str) -> bool:
        pset = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s:
            if c in pset.keys():
                stack.append(c)
            else:
                if stack and pset[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0