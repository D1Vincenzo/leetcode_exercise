#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }

        s = s[::-1]
        result = 0
        prev = 0
        for c in range(len(s)):
            if roman[s[c]] >= prev:
                result += roman[s[c]]
            else:
                result -= roman[s[c]]
            prev = roman[s[c]]

        return result
# @lc code=end

