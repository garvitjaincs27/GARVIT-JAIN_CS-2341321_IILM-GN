# 16 3Sum Closest

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('inf')
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(closest - target):
                    closest = s
                if s < target:
                    l += 1
                else:
                    r -= 1
        return closest