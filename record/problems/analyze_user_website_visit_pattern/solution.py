class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        mapper = {}
        n = len(username)
        for i in range(n):
            mapper[timestamp[i]] = (username[i], website[i])
            
        sorted_mapper = sorted(list(mapper.items()))       
        for i, val in enumerate(sorted_mapper):
            times, (name, web) = val
            username[i] = name
            timestamp[i] = times 
            website[i] = web

        user2webs = collections.defaultdict(list)
        for i in range(n):
            user = username[i]
            web = website[i]
            user2webs[user].append(web)
        
        user2seq = collections.defaultdict(set)
        for user, webs in user2webs.items():
            if len(webs) == 3:
                strseq = " ".join(webs)
                user2seq[user].add(strseq)
            elif len(webs) > 3:
                num_webs = len(webs)
                for i in range(num_webs-2):
                    for j in range(i+1, num_webs-1):
                        for k in range(j+1, num_webs):
                            strseq = " ".join([webs[i], webs[j], webs[k]])
                            user2seq[user].add(strseq)
        
        seqcnter = collections.defaultdict(int)
        for user, seqs in user2seq.items(): 
            for seq in seqs:
                seqcnter[seq] += 1
        res = ""
        maxcnt = -1
        for seq, cnt in seqcnter.items():
            if cnt > maxcnt:
                res = seq 
                maxcnt = cnt 
            elif maxcnt == cnt:
                res = min(res, seq)
                
        return res.split()
                

            