class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        while i<len(nums):
            if nums[i-1] == nums[i]:
                del nums[i]
            else:
                i+=1
        return i

            
            

            
        