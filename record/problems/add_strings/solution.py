class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        carry, i, j, res = 0, len(num1)-1, len(num2)-1, []
        
        while i >= 0 or j >=0:
            cursum = carry
            
            if i >= 0:
                cursum += ord(num1[i]) - ord('0')
            if j >= 0:
                cursum += ord(num2[j]) - ord('0')
            
            # add the digit
            res.append(cursum % 10)
            
            # update the carry
            carry = cursum // 10  
            i -= 1
            j -= 1
        
        if carry:
            res.append(carry)
            
        res.reverse()
        
        return "".join(str(x) for x in res)
            
            
        