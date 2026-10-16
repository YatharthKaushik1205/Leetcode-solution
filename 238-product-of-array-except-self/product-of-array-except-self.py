class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        answer = [0]*n
        left_product=1
        right_product=1
        for i in range(0,n):
            answer[i]=left_product
            left_product *=nums[i]
        j=n-1
        while(j>=0):
            answer[j] = answer[j]*right_product
            right_product*=nums[j]
            j-=1
        return answer
