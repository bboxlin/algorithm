class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isValid(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False 
                i += 1
                j -= 1
            return True 
            
        def find(i, curans):
            if i == len(s):
                res.append(curans.copy())
                return
            for idx in range(i, len(s)):
                if isValid(i, idx):
                    curans.append(s[i:idx+1])
                    find(idx+1, curans)
                    curans.pop()
        res = []
        find(0, [])
        return res