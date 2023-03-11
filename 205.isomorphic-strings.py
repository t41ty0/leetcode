#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        index = 1
        stock = {}
        if s == t:
            return True

        for i in range(len(s)):
            if s[i] not in stock.keys():
                if t[i] in stock.values():
                    return False
                else:
                    stock[s[i]] = t[i]
            else:
                if t[i] is not stock[s[i]]:
                    return False
        print(stock)
        return True
        
# @lc code=end

