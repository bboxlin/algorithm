class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        memo = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    
        n1 = 0
        n2 = 0
        
        m1 = 1
        for i in range(len(num1)-1, -1, -1):
            val = ord(num1[i]) - ord('0')       
            n1 = n1 + (m1*val)
            m1 = m1 * 10

        m2 = 1
        for i in range(len(num2)-1, -1, -1):
            val = ord(num2[i]) - ord('0')
            n2 = n2 + (m2*val)
            m2 = m2 * 10
        
        int_res = n1*n2
        if int_res == 0: return "0"

        str_res = ""
        while int_res:
            cur = int_res % 10 
            str_res += memo[cur]
            int_res = int_res // 10
            
        res = ""
        for i in range(len(str_res)-1, -1, -1):
            res += str_res[i]
        
        
        return res
  