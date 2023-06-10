class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        #
        # 1+2..+100 = (low+hight)*cnt/2 = (1+100)*100 / 2
        def count(h, n, index):
            cnt = 0
            if h > index:
                # 
                cnt += (h-index + h)* (index + 1) // 2
            else:
                # numbers of 1 in front 
                # (1 1) (1 2 3 4 5 6) ....
                cnt += index - h + 1
                cnt += (1+h)*h // 2
            
            if h > n-index:
                cnt += (h - (n-index) + 1 + h) * (n - index) // 2
            else:
                cnt += n - (index + h)
                cnt += (1+h)*h // 2
            return cnt - h


        left, right = 0, maxSum
        while left < right:
            mid = right - (right - left) // 2
            if count(mid, n, index) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left 
    
