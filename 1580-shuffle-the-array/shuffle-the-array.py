class Solution(object):
    def shuffle(self, nums, n):
        answer = []
        i=0
        while(i<n):
            answer.append(nums[i])
            answer.append(nums[i+n])
            i+=1
        return answer
        