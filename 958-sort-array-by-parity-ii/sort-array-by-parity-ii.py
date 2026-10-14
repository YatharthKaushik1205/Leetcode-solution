class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even_index = 0
        odd_index = 1
        a = len(nums)
        while(odd_index<a and even_index<a):
            if(nums[odd_index]%2!=0):
                odd_index+=2
            elif(nums[even_index]%2==0):
                even_index+=2
            elif(nums[even_index]%2!=0 and nums[odd_index]%2==0):
                (nums[even_index],nums[odd_index])=(nums[odd_index],nums[even_index])
                even_index+=2
                odd_index+=2
        return nums

        