class Solution:
    def longestSubarray(self, A: List[int], limit: int) -> int:
        maxd = collections.deque()
        mind = collections.deque()
        ans = 0
        l = 0
        for r, a in enumerate(A):
            while len(maxd) and a > maxd[-1]: maxd.pop()  # [max decreasing ... ]
            while len(mind) and a < mind[-1]: mind.pop()  # [min increaing ]
            maxd.append(a)
            mind.append(a)
            if  maxd[0] - mind[0] > limit:
                if maxd[0] == A[l]: maxd.popleft()
                if mind[0] == A[l]: mind.popleft()
                l += 1
            ans = max(ans, r-l+1)
        return ans