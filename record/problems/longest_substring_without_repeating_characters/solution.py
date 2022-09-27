class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ans = 0
        # charSet = set() 
        # l = 0
        # for r in range( len(s) ):   
        #     while s[r] in charSet: 
        #         charSet.remove(s[l])
        #         l += 1
        #     ans = max(ans, r-l+1)
        #     charSet.add(s[r])
        # return ans   
    
        ans = 0
        lastidx = {}
        l = 0
        for r in range( len(s) ):
            if s[r] in lastidx.keys():
                
                #l pointer only shift to right
                if lastidx[s[r]] >= l:
                    l = lastidx[s[r]] + 1
            ans = max(ans, r-l+1)
            lastidx[s[r]] = r
        return ans
            
  
      