class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # First pass: calculate prefix products for each index
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Second pass: multiply with suffix products from right to left
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res