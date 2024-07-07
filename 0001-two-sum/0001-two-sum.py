class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for i, num in enumerate(nums):
            c = target - num
            if c in num_to_index:
                return num_to_index[c], i
            num_to_index[num] = i
