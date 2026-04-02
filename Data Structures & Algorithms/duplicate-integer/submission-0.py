class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        res = False
        for n in nums:
            if dups.get(n, 0) == 0:
                dups[n] = 1
            else:
                res = True
                break
        return res