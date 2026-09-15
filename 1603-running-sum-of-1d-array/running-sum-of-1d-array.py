class Solution(object):
    def runningSum(self, nums):
        sum = 0
        answer_list = []
        for i in nums:
            sum+=i
            answer_list.append(sum)
        return answer_list
        