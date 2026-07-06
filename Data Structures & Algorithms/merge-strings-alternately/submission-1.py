class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ""
        i = 0
        while i < max(len(word1),len(word2)):
            if i >= len(word1):
                word3 += word2[i:]
                return word3
            elif i >= len(word2):
                word3 += word1[i:]
                return word3
            word3 += word1[i]
            word3 += word2[i]
            i+=1
        return word3