class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr) 
        return "".join(stack)
                


# class Solution:
#     def decodeString(self, s: str) -> str:
        
#         def helper(s, i):
#             res, mul = "", 0 
#             while i < len(s):
#                 if s[i].isdigit():
#                     # 如果s[i]数字就记录
#                     mul = mul*10 + int(s[i])
#                 elif s[i] == '[':
#                     # 如果是[ 就递归，直到 ] 返回 字符串片段
#                     i, sub = helper(s, i+1)
                    
#                     # 片段进行乘法
#                     res += mul * sub
#                     mul = 0
#                 elif s[i] == ']':
#                     #返回当前i, 非常重要
#                     return i, res
                
#                 # 普通char, 累计
#                 else:
#                     res += s[i] 
#                 i+=1
#             return res 
#         return helper(s, 0)

