class Solution:
    def partitionString(self, s: str) -> int:
        partition = set() 
        ans = 0
        for ch in s:
            if ch in partition: 
                partition.clear()
                ans += 1
            partition.add(ch)
            
        if len(partition) > 0:
            ans += 1
        return ans
