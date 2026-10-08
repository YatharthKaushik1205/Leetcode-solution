class Solution(object):
    def isPalindrome(self, s):
        n = ""
        m=""
        i=0
        if(len(s)==0):
            return True
        while(i<len(s)):
            if(s[i].isalnum()):

                m+=s[i].lower()
                i+=1
            else:
                i+=1
                continue
        a=len(m)
        n=m[::-1]
        if(n==m):
            return True
        else:
            return False
        