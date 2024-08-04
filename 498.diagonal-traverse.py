#
# @lc app=leetcode id=498 lang=python
#
# [498] Diagonal Traverse
#

# @lc code=start
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        # codnt = mat[:]
        dic = {}
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                # codnt[i][j] = i + j
                key = i + j
                if key not in dic:
                    dic[key] = []
                dic[key].append(mat[i][j])
        for k in sorted(dic.keys()):
            if k % 2 == 0:
                ans.extend(dic[k][::-1])
            else:
                ans.extend(dic[k])
        return ans
        
# @lc code=end

