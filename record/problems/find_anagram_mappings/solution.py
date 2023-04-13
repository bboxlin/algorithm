class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i, num2 in enumerate(nums2):
            if num2 not in d:
                d[num2] = []
            d[num2].append(i)
        return [d[num1].pop() for num1 in nums1]
