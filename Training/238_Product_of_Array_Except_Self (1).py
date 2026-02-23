# 238 Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums):
        res = [1]*len(nums)
        left = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]
        right = 1
        for i in reversed(range(len(nums))):
            res[i] *= right
            right *= nums[i]
        return res