class Solution:
    def countAndSay(self, n: int) -> str:
        def toCountStr(s):
            cnt_arr = []
            i = 0
            while i < len(s):
                cnt = 0
                j = i
                while j < len(s) and s[j] == s[i]:
                    cnt += 1
                    j += 1
                t = (str(cnt), s[i])
                cnt_arr.append(t)
                i = j
            return cnt_arr
        
        def toStrNum(arr):
            return "".join([ x+y for x, y in arr])
        
        curs = "1"
        for _ in range(1, n):
            cnt_arr = toCountStr(curs)
            curs = toStrNum(cnt_arr)
        return curs
            
            
            
            
          
        