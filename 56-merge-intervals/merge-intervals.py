class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        n = len(intervals)
        result = []
        for i in range(0,n):
            if(len(result)==0):
                result.append(intervals[i])
                continue
            if(result[-1][1]<intervals[i][0]):
                result.append(intervals[i])
            else:
                result[-1][0]= min(result[-1][0],intervals[i][0])
                result[-1][1]= max(result[-1][1],intervals[i][1])
        return result