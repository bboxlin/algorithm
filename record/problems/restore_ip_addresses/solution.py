class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = [] 
        if len(s) > 12: return ans
        
        def dfs(i, dot, ip):
            if dot == 4 and i >= len(s):
                ans.append(ip[:-1])
                return 
            if dot == 4:
                return 
            for j in range(i, min(i+3, len(s) )):
                curval = int(s[i:j+1])
                               # i == j indicate a single number OR not leading zero
                if curval <= 255 and (i == j or s[i] != '0'):
                    dfs(j+1, dot+1, ip+str(curval)+'.')
                    
        dfs(0, 0, "")
        return ans
                