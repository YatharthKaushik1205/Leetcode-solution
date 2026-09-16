class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        answer = [0 for i in nums]
        k=0
        for i in nums:
            for j in nums:
                if(j<i):
                    answer[k]+=1
            k+=1
        return answer