#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par_dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        
        for i in range(len(s) / 2):
            # if s[2 * i + 1] != par_dict[s[2 * i]]:
            if 
                return False
        return True
# @lc code=end

