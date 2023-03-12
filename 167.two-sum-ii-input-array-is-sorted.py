#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mnumbers = list(sorted(set(numbers)))
        print(mnumbers)
        for i in range(len(mnumbers)-1):
            for j in range(i+1, len(mnumbers)):
                if (mnumbers[i]+mnumbers[j]) == target:
                    k = numbers.index(mnumbers[i])
                    l = numbers.index(mnumbers[j])
                    break
        # print(k,l,mnumbers[i],mnumbers[j])
        return k+1, l+1
# @lc code=end
