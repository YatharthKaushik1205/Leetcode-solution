class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count =0
        for i in range(0,len(nums)):
            if nums[i]==0:
                if count>max_count:
                    max_count = count
                count =0
                continue
            count+=1
        return max(max_count,count)
        
