class Solution(object):
    def buildArray(self, target, n):
        answer =[]
        current_number = 1
        for i in target:
            while(current_number<i):
                answer.append("Push")
                answer.append("Pop")
                current_number+=1
            answer.append("Push")
            current_number+=1
        return answer
