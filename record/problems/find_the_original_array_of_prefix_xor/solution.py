class Solution:
    def findArray(self, pref: List[int]) -> List[int]:


        ans = [pref[0]]
        n = len(pref)
        
        xorsum = pref[0]
        for i in range(1, n):
            if pref[i] == 0:
                val = pref[i-1] if i > 0 else 0
                ans.append(val)
                xorsum ^= val
            else:
                 
                val = xorsum ^ pref[i]
                ans.append(val)
                xorsum ^= val
                
        print(ans) 
        return ans
            
            