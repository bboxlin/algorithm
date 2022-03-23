import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = collections.Counter(words)
        buf = sorted(freq.items(), key = lambda x:x[0])
        sorted_lst = sorted(buf, key = lambda x:x[1], reverse=True)
        
        ans = []
        for i in range(k):
            letter = sorted_lst[i][0]
            ans.append(letter)
        return ans