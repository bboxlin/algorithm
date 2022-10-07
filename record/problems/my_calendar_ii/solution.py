class MyCalendarTwo:

    def __init__(self):
        self.one = []
        self.two = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.two:
            if start < j and end > i:
                return False
        for i, j in self.one:
            if start < j and end > i:
                # the overlaped segment
                self.two.append( [max(start, i), min(end, j)] )
        self.one.append([start, end])   
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)