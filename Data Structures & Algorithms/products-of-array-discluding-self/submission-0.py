class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [1] * n

        for i in range(1, n):
            products[i] = products[i -1] * nums[i - 1]

        suffix = 1
        for i in range(n - 1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i] 
        
        return products