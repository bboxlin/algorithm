class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ans, stack = [], []
        for i, ch in enumerate(s + "I"): 
            if ch == "D": stack.append(i+1)
            else: 
                ans.append(i+1)
                while stack: ans.append(stack.pop())
        return ans 