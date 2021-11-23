class Solution:
#     def dfs(self, email, graph, visited, emails):
#         if email in visited: return
#         visited.add(email)
#         emails.append(email)
#         for nei in graph[email]:
#             self.dfs(nei, graph, visited, emails)

#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         graph = collections.defaultdict(set)
#         for acc in accounts:
#             first_email = acc[1]
#             for email in acc[2:]:
#                 graph[first_email].add(email)
#                 graph[email].add(first_email)
                
#         res = []
#         visited = set()
#         for acc in accounts:
#             emails = []
#             self.dfs(acc[1], graph, visited, emails)
#             if emails:
#                 res.append([acc[0]] + sorted(emails))
#         return res
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def union(a: int, b: int):
            uf[find(a)] = find(b)

        def find(x: int) -> int:
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        n = len(accounts)
        uf = list(range(n))
        email_dict = {}  # key is email, value is the `first` index of accounts which has the key email
        for i in range(n):
            account = accounts[i]
            for j in range(1, len(account)):
                if account[j] not in email_dict:
                    email_dict[account[j]] = i
                else:
                    union(email_dict[account[j]], i)
        graphs = collections.defaultdict(list)
        for i in range(n):
            graphs[find(i)].append(i)
        ans = []
        for idx, idx_list in graphs.items():
            cur = [accounts[idx][0]]
            emails = set()
            for i in idx_list:
                emails.update(accounts[i][1:])
            emails = list(emails)
            emails.sort()
            cur.extend(emails)
            ans.append(cur)
        return ans

    
