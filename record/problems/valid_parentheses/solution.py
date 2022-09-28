class Solution:
    def isValid(self, s: str) -> bool:
        pset = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c in pset.values():
                stack.append(c)
            else:
                if stack and stack[-1] == pset[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0