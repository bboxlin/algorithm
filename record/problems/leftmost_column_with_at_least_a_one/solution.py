# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        rows, cols = binaryMatrix.dimensions()
        i, j = 0, cols - 1

        pos = float('inf')
        
        while i < rows and j >= 0:
            if binaryMatrix.get(i, j) == 0:
                i += 1
            else:
                pos = min(pos, j)
                j -= 1
        
        return pos if pos != float('inf') else -1

        
        
        
        
        
#         length = binaryMatrix.dimensions()
#         l, r = 0, length[1]-1
        
#         pos = float('inf')
#         for i in range(length[0]):
#             while l <= r:
#                 mid = (l + r) >> 1
#                 if binaryMatrix.get(i,mid) == 1:
#                     pos = min(mid, pos)
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#             l, r = 0, length[1]-1

#         if pos != float('inf'):
#             return pos
#         else:
#             return -1