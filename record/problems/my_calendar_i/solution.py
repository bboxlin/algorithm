from sortedcontainers import SortedList


class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        
        start_idx = SortedList.bisect_right(self.calendar, start)
        end_idx = SortedList.bisect_left(self.calendar, end)
        if start_idx == end_idx and start_idx % 2 == 0:
            self.calendar.add(start)
            self.calendar.add(end)
            return True 
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)