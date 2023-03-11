#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        counter = []
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                flag = True
            elif arr[i] < arr[i+1]:
                flag = False
            elif arr[i] > arr[i+1] and flag == True:

        
# @lc code=end
