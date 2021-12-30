class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        remainder = 1
        length_N = 1

        seen_remainders = set()

        while remainder%K != 0:
            N = remainder*10 + 1
            remainder = N%K
            length_N += 1

            if remainder in seen_remainders:
                return -1
            else:
                seen_remainders.add(remainder)

        return length_N