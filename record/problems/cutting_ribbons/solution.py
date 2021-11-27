class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:    
        def canCut(length):
            count = 0
            for r in ribbons:
                # 一根绳子被剪后会产生多个绳子, 如8米绳子可剪成4个2米(二分猜测长度), 加起来最后判断满足2米的绳子数量是否达到k.
                count += r//length
            return count >= k
        
        # l <= 绳子的长度范围 <=r
        l, r = 1, 100000
        res = 0
        while l <= r:
            mid = l+r >> 1
            if canCut(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res
        
        
        # 查询最大右边界
        # while l < r:
        #     mid = l + ((r - l) >> 1) + 1;
        #     if canCut(mid):
        #         l = mid
        #     else:
        #         r = mid - 1
        # return l