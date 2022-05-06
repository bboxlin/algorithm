class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # to store (val, freq)
        for c in s:
            if stack and stack[-1][0] == c:
                val, freq = stack[-1]
                tup = (val, freq+1)
                stack.append(tup)
            else:
                tup = (c, 1)
                stack.append(tup)
            if stack and stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()           
        return "".join([c for c,freq in stack])
                