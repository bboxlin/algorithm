class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:   
        stack = []
        res = [0]*n
        prev_start_time = 0
        
        for log in logs:
            _id, runtype, time = log.split(":")
            _id, time = int(_id), int(time)
            
            if runtype == "start":
                if stack:
                    pre_id = stack[-1]
                    res[pre_id] += time - prev_start_time
                stack.append(_id)
                prev_start_time = time
            else:
                res[stack.pop()] += time - prev_start_time + 1
                prev_start_time = time + 1

        return res
