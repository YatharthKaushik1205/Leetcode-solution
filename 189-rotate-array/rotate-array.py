class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        for i in range(0,n//2):
            (nums[i],nums[n-i-1])=(nums[n-i-1],nums[i])
        for i in range(0,k//2):
            (nums[i],nums[k-i-1])=(nums[k-i-1],nums[i])
        i=k
        j=n-1
        while(i<j):
            (nums[i],nums[j]) = (nums[j],nums[i])
            i+=1
            j-=1
        return nums