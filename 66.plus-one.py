#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        digits.reverse()
        for i in range(len(digits)):
            num += digits[i] * (10 ** i)
        num = str(num + 1)
        num_list = []
        for j in range(len(num)):
            num_list.append(int(num[j]))
        
        return num_list

# @lc code=end

