class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        a = len(heights)
        count = 0
        for i in range(0,a):
            if heights[i]!=expected[i]:
                count+=1
        return count