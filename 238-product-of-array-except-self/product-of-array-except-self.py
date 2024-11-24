class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Calculate left products and store in result
        for i in range(1, n):
            result[i] = nums[i - 1] * result[i - 1]

        # Calculate right products and multiply with left products in result
        right_prod = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_prod
            right_prod *= nums[i]

        return result
