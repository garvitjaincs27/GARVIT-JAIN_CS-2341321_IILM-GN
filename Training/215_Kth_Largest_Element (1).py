# 215 Kth Largest Element

class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]