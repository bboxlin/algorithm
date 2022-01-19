class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_size = sum(data)
        max_window_size = 0
        cur_window_size = 0
        for i in range(len(data)):
            cur_window_size += data[i]
            if i >= window_size:
                cur_window_size -= data[i-window_size]
            max_window_size = max(max_window_size, cur_window_size)
        # max ones - max size of window of ones = numbers of zero in the window needed to be swap
        return window_size - max_window_size
                