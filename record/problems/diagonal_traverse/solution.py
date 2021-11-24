class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         Row, Col = len(mat), len(mat[0])
#         res = []
#         memo = collections.defaultdict(list)
#         for i in range(Row):
#             for j in range(Col):
#                 memo[i+j].append(mat[i][j])
        
#         for k,v in memo.items():
#             if k % 2 == 0:
#                 res.extend(reversed(v))
#             else:
#                 res.extend(v)
#         return res
        r, c, Row, Col = 0,0, len(mat), len(mat[0])
        res = [0]*(Row*Col)
        for i in range(len(res)):
            res[i] = mat[r][c]
            if (r+c) % 2 == 0:
                if c == Col - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == Row-1:
                    c += 1
                elif c == 0:
                    r += 1
                else: 
                    r += 1
                    c -= 1
        return res
        
        