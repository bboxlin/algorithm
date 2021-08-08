class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        memo = {}
        t = 0
        for i in range(len(releaseTimes)):
            key = keysPressed[i]
            if key in memo:
                memo[key] = max(releaseTimes[i] - t, memo[key])
            else:
                memo[key] = releaseTimes[i] - t
            t = releaseTimes[i]

        tmax = max(memo.values())
        keymax = "0" #lowest ascii code
        for k,v in memo.items():
            if v == tmax:
                keymax = max(k,keymax)
        return keymax
            