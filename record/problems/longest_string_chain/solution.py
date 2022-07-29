class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key = lambda x: len(x)) 
        resultmap = {}
        ans = 0
        for word in words:
            cur_len = 1
            for i in range( len(word) ):
                newword = word[:i] + word[i+1:]
                if newword in resultmap.keys():
                    cur_len = max(cur_len, resultmap[newword] + 1)
            resultmap[word] = cur_len
            ans = max(ans, cur_len)
        return ans