# 229 Majority Element II

class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        c1 = c2 = None
        v1 = v2 = 0
        for n in nums:
            if n == c1:
                v1 += 1
            elif n == c2:
                v2 += 1
            elif v1 == 0:
                c1, v1 = n, 1
            elif v2 == 0:
                c2, v2 = n, 1
            else:
                v1 -= 1
                v2 -= 1
        return [n for n in (c1, c2) if nums.count(n) > len(nums)//3]