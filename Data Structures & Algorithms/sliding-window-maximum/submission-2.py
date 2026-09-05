from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for i in range(len(nums)):
            # Remove indices that are outside the window
            while q and q[0] < i - k + 1:
                q.popleft()

            # Remove smaller values from the back
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            # Add current index
            q.append(i)

            # Once we have a full window, record the maximum
            if i >= k - 1:
                result.append(nums[q[0]])

        return result
