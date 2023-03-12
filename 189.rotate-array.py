#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k is not 0 and len(nums) > 1:
            nums[0:0] = nums[-abs(k):]
            print(nums)
            del nums[len(nums) - k: len(nums)]
        # print(nums)


# @lc code=end
