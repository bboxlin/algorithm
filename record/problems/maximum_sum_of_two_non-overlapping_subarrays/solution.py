class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], a: int, b: int) -> int:
        prefix = [0]
        maxa = maxb = summ = 0
        for x in A:
            prefix.append(prefix[-1] + x)
        # b after a
        for i in range(a, len(prefix) - b):
            maxa = max(maxa, prefix[i] - prefix[i - a])
            summ = max(summ, maxa + prefix[i + b] - prefix[i])

        # a after b
        for i in range(b, len(prefix) - a):
            maxb = max(maxb, prefix[i] - prefix[i - b])
            summ = max(summ, maxb + prefix[i + a] - prefix[i])
        return summ

