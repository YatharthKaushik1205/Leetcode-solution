class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0
        max_sum = nums[0]
        n = len(nums)
        if n==1:
            return nums[0]
        for i in range(n):
            current_sum += nums[i]
            max_sum = max(current_sum,max_sum)
            if current_sum<0:
                current_sum = 0
        return max_sum