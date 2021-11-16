class Solution:
    def calculate(self, s: str) -> int:
        prevOp = '+'
        stack = []
        num,i,n = 0,0,len(s)-1
        for c in s:
            
            if c.isdigit() and c != ' ':
                num = num*10 + ord(c) - ord('0')
            if c in '+-*/' or i == n:
                if i ==n :print(num)
                if prevOp == '+': stack.append(num)
                elif prevOp == '-': stack.append(-num)
                elif prevOp == '*': 
                    stack.append(stack.pop()*num)
                else:stack.append(int(stack.pop()/num))
                prevOp = c
                num = 0
            i += 1
        return sum(stack)