class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # first check if there exist a (, 
        # check if upcoming )
        # ac(ddd)ss
        
        # ( , 放入栈中
        # 如果遇到 )  栈pop
        # ()(()) 
        # )(
        
        # (i,括号)
        stack = [] #parenthesis
        sl = list(s)
        for i in range(len(sl)): 
            if sl[i] == ')':
                if stack and stack[-1][1] == '(': 
                    stack.pop()
                else:
                    sl[i] = ""
            elif sl[i] == '(':
                stack.append((i, sl[i]))
        
        # 2,(  3,(  
        for i, p in stack:
            sl[i] = ""
            
        return "".join(sl)
        #))(( 
        # (( 
        #