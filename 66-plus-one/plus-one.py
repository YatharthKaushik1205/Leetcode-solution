class Solution(object):
    def plusOne(self, digits):
        answer=[]
        for j in range(len(digits)-1,-1,-1):
            if(digits[j]<9):
                digits[j]+=1
                return digits
            digits[j]=0
            j-=1
        digits.insert(0,1)
        return digits


        
        