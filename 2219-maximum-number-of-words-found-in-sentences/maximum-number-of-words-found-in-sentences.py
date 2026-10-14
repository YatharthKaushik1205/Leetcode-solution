class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        word_count = 0 
        max_word_count = 0
        for sentence in sentences:
            word_count = sentence.count(' ')+1
            if word_count>max_word_count:
                max_word_count = word_count
        return max_word_count