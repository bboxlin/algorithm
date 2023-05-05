class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        Rq = deque([])
        Dq = deque([])
        for i,c in enumerate(senate):
            if c == 'R': Rq.append(i)
            else: Dq.append(i)

        while Rq and Dq:
            ri = Rq.popleft()
            di = Dq.popleft()
            if ri < di:
                Rq.append(ri + n)
            else:
                Dq.append(ri + n)
        return 'Radiant' if Rq else 'Dire'

        