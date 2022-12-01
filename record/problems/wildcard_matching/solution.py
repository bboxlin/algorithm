class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        i, j = 0, 0
        di, dj = -1, -1  #pointers used for backtrack 
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                di = i
                dj = j
                j += 1
            elif di != -1:
                di += 1
                i = di  # if here then try * place one more i
                j = dj + 1  # trace back to original j
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)
    
        # @cache
        # def dfs(i, j):
        #     """
        #     双指针回溯
        #     base case 2 种情况
        #         1. j先到len(p)那么i如果此时也到len(s)则匹配
        #         2. i先到len(s)，因为p[j]可以是*，*可以代表空,那么如果p[j:]都是*则匹配
        #     贪心策略
        #     - 字母能相互对应肯定先对应，i+1,j+1 
        #     - p[j]如果是*, 有两种情况，让*匹配空或者多个s的字母
        #     - 当前不匹配自然到此为止，停止当前分支的递归
        #     """
        #     if j == len(p):
        #         return i == len(s)
        #     if i == len(s):
        #         isrestStar = True 
        #         for dj in range(j, len(p)):
        #             isrestStar &= p[dj] == '*'
        #         return isrestStar
        #     if s[i] == p[j] or p[j] == '?':
        #         return dfs(i+1, j+1)
        #     elif p[j] == '*':
        #         return dfs(i, j+1) or dfs(i+1, j)  
        #     else:
        #         # not match ret False 
        #         return False    
        # return dfs(0, 0)