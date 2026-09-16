class Solution(object):
    def buildArray(self, nums):
        answer = []
        a = len(nums)
        for i in range(0,a):
            answer.append(nums[nums[i]])
        return answer
        