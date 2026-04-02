class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in diff_dict:
                return [diff_dict[nums[i]], i]
            diff_dict[diff] = i
        return [-1, -1]