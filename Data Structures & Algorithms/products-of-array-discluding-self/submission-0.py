class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_dict = defaultdict(lambda: 1)
        prod = 1
        for i in range(len(nums)):
            prod_dict[i] *= prod
            prod *= nums[i]
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod_dict[i] *= prod
            prod *= nums[i]
        return [val for val in prod_dict.values()]