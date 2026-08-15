class Solution(object):
    def isHappy(self, n):
        Sum=n
        n1=n
        Sum_collection=[]
        while (Sum!=1):
            if Sum in Sum_collection:
                return False
                break
            else:
                Sum_collection.append(Sum)
            Sum=0
            while(n1!=0):
                r=n1%10
                Sum=Sum+r**2
                n1=n1//10
            n1=Sum
        return True