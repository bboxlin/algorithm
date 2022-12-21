class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(idx):
            visited.add(idx)
            for k in rooms[idx]:
                if k in visited:
                    continue
                dfs(k)
        visited = set() 
        dfs(0)
        return len(visited) == len(rooms)