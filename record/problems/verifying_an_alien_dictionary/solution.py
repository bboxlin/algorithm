class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lookup = {}
        for i, c in enumerate(order):
            lookup[c] = i
            
        n = len(words)
        for i in range(1, n):
            cur = words[i]
            prv = words[i-1]

            brk = False
            m = min( len(cur), len(prv) )
            for j in range(m):
                if lookup[cur[j]] == lookup[prv[j]]:
                    continue
                if lookup[cur[j]] > lookup[prv[j]]:
                    brk = True
                    break
                if lookup[cur[j]] < lookup[prv[j]]:
                    return False
            # cur >= prv then 
            if not brk and len(prv) > len(cur):
                return False
        return True
