class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        counter = Counter(nums)
        return counter[target] > (n // 2)