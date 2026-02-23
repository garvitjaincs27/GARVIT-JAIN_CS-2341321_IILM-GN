# 2149 Rearrange Array Elements by Sign

class Solution:
    def rearrangeArray(self, nums):
        pos = [n for n in nums if n > 0]
        neg = [n for n in nums if n < 0]
        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res