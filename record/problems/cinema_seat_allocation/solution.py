class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        table = defaultdict(set)
        for i, j in reservedSeats:
            if j in [2,3,4,5]:
                table[i].add(0)
            if j in [4,5,6,7]:
                table[i].add(1)
            if j in [6,7,8,9]:
                table[i].add(2)
                
        total = 2*n
        for row in table.keys():
            if len(table[row]) == 3:
                total -= 2
            else:
                total -= 1
 
        return total