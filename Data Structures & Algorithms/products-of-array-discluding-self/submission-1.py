class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = []
        prod = 1
        for i in range(len(nums)):
            prods.append(1)
            prods[i] *= prod
            prod *= nums[i]
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prods[i] *= prod
            prod *= nums[i]
        return prods