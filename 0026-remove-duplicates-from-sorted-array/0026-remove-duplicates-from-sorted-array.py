class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicates = 0
        i=1
        while i<len(nums):
            if nums[i-1] == nums[i]:
                del nums[i]
                duplicates += 1
            else:
                i+=1
        k = len(nums)
        return k

            
            

            
        