class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        res = 0
        rows = set()
        cols = set()
        rcnt = ccnt = n
        for i in range(len(queries)-1, -1, -1):
            typ, idx, v = queries[i]
            if typ == 0:
                if idx not in rows:
                    res += v * ccnt
                    rows.add(idx)
                    rcnt -= 1
            else:
                if idx not in cols:
                    res += v * rcnt
                    cols.add(idx)
                    ccnt -= 1
        return res


        
