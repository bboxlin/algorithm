class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = 0
        arr = [0] + arr + [0]
        for i, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                cur_i = stack.pop()
                                    # left                 right
                res += arr[cur_i] * (cur_i - stack[-1])* (i - cur_i)
            stack.append(i)
        return res%(10**9+7)
