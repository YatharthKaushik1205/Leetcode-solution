class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        answer = []
        for i in candies:
            if i+extraCandies >= max(candies):
                answer.append(True)
            else:
                answer.append(False)
        return answer

        