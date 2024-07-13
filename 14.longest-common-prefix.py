#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        count = 0
        shortest_len = min([len(s) for s in strs])
        for i in range(shortest_len):
            for j in strs:
                if j[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix
# @lc code=end

