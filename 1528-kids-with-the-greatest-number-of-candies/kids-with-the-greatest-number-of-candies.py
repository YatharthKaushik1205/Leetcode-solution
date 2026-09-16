class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        answer = []
        maximum = max(candies)
        for i in candies:
            if i+extraCandies >= maximum:
                answer.append(True)
            else:
                answer.append(False)
        return answer

        