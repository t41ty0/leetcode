#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        inquality = []

        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                inquality.append(1)
            elif arr[i] < arr[i+1]:
                inquality.append(0)
            elif arr[i] == arr[i+1]:
                inquality.append(2)

        print(inquality)
        count = 0
        result = []

        for i in range(len(inquality)-1):
            print(i, count)
            if inquality[i] != inquality[i+1] and inquality[i+1] is not 2:
                count += 1
            elif inquality[i] == inquality[i+1]:
                result.append(count)
                count = 0
            else:
                print('what!?')
        result.append(count)
        print(result)
        return max(result)


# @lc code=end
