class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return -1
        arr = []
        for i in range(3):
            arr.append(nums[i])
        arr.sort()
        return arr[1]