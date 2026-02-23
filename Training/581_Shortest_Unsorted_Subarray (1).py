# 581 Shortest Unsorted Subarray

class Solution:
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)
        l, r = 0, len(nums)-1
        while l < len(nums) and nums[l] == sorted_nums[l]:
            l += 1
        while r > l and nums[r] == sorted_nums[r]:
            r -= 1
        return 0 if r <= l else r-l+1