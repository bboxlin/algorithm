class SnapshotArray:
    def __init__(self, length: int):
        self.id = 0
        self.snapshot = [ [[0,0]] for _ in range(length)]

    # the id of snapshot[index] is increasing.... 
    def set(self, index: int, val: int) -> None:
        if self.snapshot[index][-1][0] == self.id:
            self.snapshot[index][-1][1] = val
            return
        self.snapshot[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        snaps = self.snapshot[index]
        left, right = 0, len(snaps) - 1
        idx = -1
        while left <= right:
            mid = (left + right) // 2
            if snaps[mid][0] <= snap_id:
                # because we dont capture all value in each snapshot
                # when snapshot we just self.id + 1
                # so the most recent version is the one we looking for.
                idx = mid
                left = mid + 1
            else:
                right = mid - 1
        if idx == -1: return 0
        return snaps[idx][1]
"""
0:15 -0 
0:15 -1
0:15 -2
"""

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

 