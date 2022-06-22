class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        kx, ky = king   
        def canAttack(qx, qy):
            if qx == kx or qy == ky:
                return True
            if abs(kx - qx) == abs(ky - qy):
                return True
            return False
        
        attacker = set()
        for qx, qy in queens:
            if canAttack(qx, qy):
                attacker.add((qx,qy))
        
        res = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in range(1,8):
                    x, y = kx + i*k, ky + j*k
                    if (x,y) in attacker:
                        res.append([x, y])
                        break
        return res
                        
                        
            
        
        
            