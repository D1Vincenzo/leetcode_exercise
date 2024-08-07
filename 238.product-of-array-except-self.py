#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        # 这个真特么难 
        # https://youtu.be/5bS636lE_R0?si=zGheZ8x9TWYLXebq
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        right = 1
        for j in range(len(nums) - 2, -1, -1):
            right *= nums[j + 1]
            ans[j] *= right
        return ans
        
        
# @lc code=end

