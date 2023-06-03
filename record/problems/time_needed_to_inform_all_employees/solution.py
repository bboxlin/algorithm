class Solution:
    # DAG problem
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for me, mymanager in enumerate(manager):
            graph[mymanager].append(me)

        res = 0
        q = deque([ (headID, 0) ])
        while q:
            manager, time = q.popleft()
            res = max(res, time)
            for sub in graph[manager]:
                q.append( (sub, time+informTime[manager]) )
        return res

 