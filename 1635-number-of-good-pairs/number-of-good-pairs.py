class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = [0]*101
        count = 0 
        for num in nums:
            count+=freq[num]
            freq[num]+=1
        return count
        