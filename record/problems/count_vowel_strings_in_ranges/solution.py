class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        presum = []
        pre = 0
        vowels = "aeiou"
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                pre += 1
            presum.append(pre)
        
        ans = []
        for i, j in queries:
            if i - 1 >= 0:
                cnt = presum[j] - presum[i-1]
                ans.append(cnt)
            else:
                ans.append(presum[j])
        return ans