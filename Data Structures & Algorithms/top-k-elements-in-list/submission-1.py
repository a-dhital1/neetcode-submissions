import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if not nums:
            return nums

        num_count = {}

        for i in nums:
            num_count[i] = num_count.get(i, 0) + 1

        heap = []

        for num, count in num_count.items():
            heapq.heappush(heap, [count, num])

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]
            

        