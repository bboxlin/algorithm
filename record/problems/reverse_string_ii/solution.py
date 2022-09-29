class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        lists = list(s)
        for i in range(0, len(s), 2*k):
            l, r = i, min(i+k-1, len(s)-1)
            while l<r:
                lists[l], lists[r] = lists[r], lists[l]
                l += 1
                r -= 1
        return "".join(lists)
        