#
# @lc app=leetcode id=724 lang=python
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in range(len(nums)):
            if sum(nums[:n]) == sum(nums[(n + 1):]):
                pivot = n
                break
            else:
                pivot = -1
        return pivot
# @lc code=end