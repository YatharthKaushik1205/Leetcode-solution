class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t)!=len(s):
            return False
        freq = [0]*26
        for i in range(len(s)):
            freq[ord(s[i])-ord('a')]+=1
            freq[ord(t[i])-ord('a')]-=1
        for count in freq:
            if count!=0:
                return False
        return True