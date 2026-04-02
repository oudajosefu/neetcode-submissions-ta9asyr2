class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        top_k = []
        for key, val in count.items():
            heapq.heappush(top_k, (val, key))
            if len(top_k) > k:
                heapq.heappop(top_k)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(top_k)[1])
        return res