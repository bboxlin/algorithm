class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        topRemove = False
        for c in s:
            if topRemove:
                stack.pop()
                topRemove = False
            if stack and stack[-1] == c:
                topRemove = True
                continue 
            stack.append(c)
        if topRemove:
                stack.pop()
        return "".join(stack)