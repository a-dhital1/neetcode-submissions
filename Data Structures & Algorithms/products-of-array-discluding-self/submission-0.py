class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        result = [0] * n

        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for j in range(n-1, -1, -1):
            result[j] *= right_product
            right_product *= nums[j]

        return result