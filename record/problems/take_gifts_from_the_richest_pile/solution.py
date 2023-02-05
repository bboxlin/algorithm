class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k:
            gifts.sort()
            rem = math.floor(gifts[-1] ** 0.5)
            gifts[-1] = rem
            k -= 1
        return sum(gifts)