class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq = "123456789"
        len_low, len_high = len(str(low)), len(str(high))
         
        res = []
        for length in range(len_low, len_high + 1):
            i = 0
            while i + length <= len(seq):    
                num = int(seq[i: i+length])
                if low <= num <= high:
                    res.append(num)
                i += 1
        return res
        
#         out = []
#         queue = deque(range(1,10))
#         while queue:
#             elem = queue.popleft()
#             if low <= elem <= high:
#                 out.append(elem)
#             last = elem % 10
#             if last < 9: queue.append(elem*10 + last + 1)
                    
#         return out
            