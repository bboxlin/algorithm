class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # [[1,2,3],[4,5],[1,2,3]]
        #   curmax
        #   curmin
        # res = max{ curmax - min, max - curmin}
        res = 0
        minn = math.inf
        maxx = -math.inf
        for arr in arrays:
            curmax = arr[-1]
            curmin = arr[0]
            res = max(res, max(curmax - minn, maxx - curmin))
            maxx = max(maxx, curmax)
            minn = min(minn, curmin)
        return res


 