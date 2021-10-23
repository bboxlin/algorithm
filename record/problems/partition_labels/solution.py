class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt = Counter(s)
        myset = {}
        partition = []
        result = []
        for letter in s:
            if letter not in myset:
                myset[letter] = cnt.get(letter)
            partition.append(letter)
            myset[letter] -= 1
            if sum(myset.values()) == 0:
                result.append(len(partition))
                partition.clear()
        return result


