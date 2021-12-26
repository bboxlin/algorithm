class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        sl = list(s)
        for i, c in enumerate(sl):
            if c == '(':
                stack.append((i,c))
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    sl[i] = ""
        for i, openp in stack:
            sl[i] = ""
        return "".join(sl)        
        

    
        
