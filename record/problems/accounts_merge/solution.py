class Solution:
    # time: O(NK log NK), N = numbers of account , K max length of an account
    # space: O(log NK)
    def dfs(self, email, graph, visited, emails):
        if email in visited: return
        visited.add(email)
        emails.append(email)
        for nei in graph[email]:
            self.dfs(nei, graph, visited, emails)

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        for acc in accounts:
            first_email = acc[1]
            for email in acc[2:]:
                graph[first_email].add(email)
                graph[email].add(first_email)
                
        res = []
        visited = set()
        for acc in accounts:
            emails = []
            self.dfs(acc[1], graph, visited, emails)
            if emails:
                res.append([acc[0]] + sorted(emails))
        return res


    
