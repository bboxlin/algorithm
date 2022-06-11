class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # lastIdxMemo = { c:i for i, c in enumerate(s)}
        # ans = []
        # l, r = 0, 0
        # for i, c in enumerate(s):
        #     r = max(r, lastIdxMemo[c])
        #     if i == r:
        #         ans.append(r-l+1)
        #         l = r + 1
        # return ans
        freq = collections.Counter(s)
        cnter, partition = {}, []
        ans = []
        l = 0
        for i, c in enumerate(s):
            if c not in cnter.keys():
                cnter[c] = freq[c]
            cnter[c] -= 1
            partition.append(c)
            
            if sum(cnter.values()) == 0:
                ans.append(len(partition))
                partition.clear()
        return ans