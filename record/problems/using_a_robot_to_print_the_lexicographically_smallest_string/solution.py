class Solution:
    def robotWithString(self, s: str) -> str:
        """
        t is a stack, every char goes into t
        dic to record the frequency
        once the top of t is the min compare with the res, pop off the t
        
        lastly, if theres element in t, pop off them
        """
        dic, t, ans = Counter(s), [], []
        for char in s:
            t.append(char)
            if dic[char] == 1:
                del dic[char]
            else:
                dic[char] -= 1
            while dic and t and min(dic) >= t[-1]:
                ans += t.pop()
 
        while t:
            ans.append(t.pop())
        return ''.join(ans)
            
            
            
                