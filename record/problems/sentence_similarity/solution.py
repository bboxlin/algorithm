class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        sim = defaultdict(set)
        for x, y in similarPairs:
            sim[x].add(y)
            sim[y].add(x)
        if len(sentence1) != len(sentence2): 
            return False 
        n = len(sentence1)
        for i in range(n):
            w1 = sentence1[i]
            w2 = sentence2[i]
            if w1 == w2 or w2 in sim[w1]:
                continue 
            return False 
       
        return True

