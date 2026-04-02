class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        top_k = heapq.nlargest(k, [(val, key) for key, val in count.items()])
        return [key for _, key in top_k]