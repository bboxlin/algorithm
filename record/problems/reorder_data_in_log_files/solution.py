class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def is_digitLog(log):
            lst = log.split()
            return lst[1].isdigit()
            
        buffer_letter = []
        buffer_digit = []
        for log in logs:
            if is_digitLog(log):
                buffer_digit.append(log)
            else:
                buffer_letter.append(log)
        
        buffer_letter.sort(key = lambda x: x.split()[0])
        buffer_letter.sort(key = lambda x: x.split()[1:])
         
        
        return buffer_letter + buffer_digit