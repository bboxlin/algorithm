class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        # O(k*n), k = 最高频率的数量
        # [1,2,3,4,5]
        freqTable = Counter(nums)
        maxFreq = max(freqTable.values())
        maxFreqNum = []
        for num, freq in freqTable.items():
            if maxFreq == freq:
                maxFreqNum.append(num)
        if maxFreq == 1: return 1
        n = len(nums)
        ans = n
        while len(maxFreqNum) > 0:
            curMaxNum = maxFreqNum.pop()
            i, j = 0, n-1
            while i < n and nums[i] != curMaxNum:
                i += 1
            while j < n and nums[j] != curMaxNum:
                j -= 1
            curlen = j - i + 1
            ans = min(ans, curlen)
        return ans
                
            
            