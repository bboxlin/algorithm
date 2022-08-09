class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # time O(n^2)
        # space O(n)
        arr.sort()
        n = len(arr)
        dp = [1] * n
        mod = 10**9 + 7
        visitedmap = {arr[0] : 0}
        for i in range(1, n):
            a = arr[i]
            for j in range(i):
                b = arr[j]
                if a % b == 0:
                    res = a // b
                    if res in visitedmap.keys():
                        k = visitedmap[res]
                        dp[i] += dp[j] * dp[k]  # two subtree combinations
            visitedmap[a] = i  # since every val is unique, this tracks index of every visited val
        print(dp)
        return sum(dp) % mod
            