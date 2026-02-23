# 34 First and Last Position in Sorted Array

class Solution:
    def searchRange(self, nums, target):
        def find(left):
            l, r = 0, len(nums)
            while l < r:
                mid = (l+r)//2
                if nums[mid] > target or (left and nums[mid]==target):
                    r = mid
                else:
                    l = mid+1
            return l
        left = find(True)
        right = find(False)-1
        if left<=right and right<len(nums) and nums[left]==target:
            return [left, right]
        return [-1,-1]