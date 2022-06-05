class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i, write = 0, 0 
        while i < n:
            j = i 
            while j < n and chars[j] == chars[i]:
                j += 1
            chars[write] = chars[i]
            write += 1
            if j-i > 1:
                cnt = j - i
                begin = write
                while cnt > 0:
                    num = str(cnt % 10)
                    cnt = cnt // 10
                    chars[write] = num
                    write += 1
                end = write - 1 
                
                while begin < end:
                    chars[begin], chars[end] = chars[end], chars[begin]
                    begin += 1
                    end -= 1
                
            i = j 
        return write
 
                        
                