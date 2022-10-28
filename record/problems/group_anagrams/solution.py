class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 每个element sort 一遍
        # ？ 如何把相同的放一块
        # dic = defaultdict(list)
        # for word in strs:
        #     k = tuple(sorted(list(word)))
        #     dic[k].append(word)
        # return dic.values()
        
        # 26*n = O(n)
        dic = defaultdict(list)
        for word in strs:
            keylist = [0] * 26
            for c in word:
                idx = ord(c) - ord("a")
                keylist[idx] += 1
            k = tuple(keylist)
            dic[k].append(word)
        return dic.values()
            
        