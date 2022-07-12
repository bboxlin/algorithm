class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        maxdamage = max(damage) 
        if maxdamage > armor:
            return sum(damage) - armor + 1
        else:
            return sum(damage) - maxdamage + 1