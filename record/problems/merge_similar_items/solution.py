class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        for x, y in items1:
            dic[x] += y
        for x, y in items2:
            dic[x] += y
        ans = []
        for x, y in sorted(dic.items()):
            ans.append([x,y])
        return ans