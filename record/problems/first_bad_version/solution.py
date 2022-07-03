# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        res = 0
        l, r = 1, n
        while l <= r:
            mid = l+r>>1
            if isBadVersion(mid):
                r = mid - 1
                res = mid 
            else:
                l = mid + 1
        return res
        