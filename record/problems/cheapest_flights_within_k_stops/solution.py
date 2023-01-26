class Solution:
    """
    Bellman - Ford
    liked BFS
    time:  O(Ek)
    """
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        destinations = collections.defaultdict(list)
        for s, d, cost in flights:
            destinations[s].append([d, cost])
        
        min_distance = float('inf')
        cost_to_destination = collections.defaultdict(int) # Keep only the min cost
        queue = collections.deque()
        queue.append([src, 0])
        stops = 0
        
        while queue and stops <= k:
            for _ in range(len(queue)):
                current, current_cost = queue.popleft()
                for destination, cost in destinations[current]:
                    # 截肢 防止TLE
                    if destination in cost_to_destination and current_cost + cost > cost_to_destination[destination]:
                        continue
                    cost_to_destination[destination] = current_cost + cost
                    if destination == dst:
                        min_distance = min(min_distance, current_cost + cost)
                        continue # 再截一层 
                    queue.append([destination, current_cost + cost])
            stops += 1
        
        return min_distance if min_distance != float('inf') else -1

 