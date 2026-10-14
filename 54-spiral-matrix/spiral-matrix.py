class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        s_col = 0 
        e_col = len(matrix[0])-1
        s_row = 0
        e_row = len(matrix)-1
        while(s_col<=e_col and s_row<=e_row):
            #top 
            for i in range(s_col,e_col+1):
                ans.append(matrix[s_row][i])
            #right
            for i in range(s_row+1,e_row+1):
                ans.append(matrix[i][e_col])
            #bottom
            for i in range(e_col-1,s_col-1,-1):
                if(s_row==e_row):
                    break
                ans.append(matrix[e_row][i])
            #left
            for i in range(e_row-1,s_row,-1):
                if(s_col==e_col):
                    break
                ans.append(matrix[i][s_col])
            s_row+=1
            e_row-=1
            s_col+=1
            e_col-=1
        return ans

        