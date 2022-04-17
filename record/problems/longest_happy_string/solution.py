class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:   
        stack = [('a', a), ('b', b), ('c', c)]
        stack.sort(key = lambda x: x[1])
        max_cnt, max_cha = stack[-1][1], stack[-1][0]
        
        # prepare the buffer
        buf = [[max_cha, max_cha] for _ in range(max_cnt // 2)]
        if max_cnt % 2 != 0: buf.append([max_cha])
        stack.pop()
        
        idx = 0
        while stack:
            curchar, curmax = stack[-1][0], stack[-1][1]
            ans_len = len(buf)
            while curmax:
                buf[idx % ans_len].append(curchar)
                idx += 1
                curmax -= 1
            stack.pop()
        
        # check for potential stop point
        ans = "".join(["".join(lst) for lst in buf])
        for i in range(2, len(ans)):
            if ans[i] == ans[i-1] == ans[i-2]:
                return ans[:i]
        return ans
        
        
            
        
               