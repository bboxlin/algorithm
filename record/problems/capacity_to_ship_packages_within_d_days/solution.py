class Solution:
    """
    Hint:
    Binary search on the answer. We need a function possible(capacity) which returns true  
    if and only if we can do the task in D days.
    """
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(capacity):
            cnt = 1
            acc = 0
            for w in weights:
                acc += w
                if acc > capacity:
                    cnt += 1
                    acc = w
            return cnt <= days

        lo, hi = max(weights), sum(weights)
        while lo < hi:
            cap = (lo + hi) // 2
            if possible(cap):
                hi = cap # try to most left
            else:
                lo = cap + 1
        return lo
                

