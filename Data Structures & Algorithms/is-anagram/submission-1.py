class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana = {}
        ana2 = {}
        for x in s:
            if ana.get(x) is None:
                ana[x] = 1
            else:
                ana[x] = ana.get(x) + 1
        for y in t:
            if ana2.get(y) is None:
                ana2[y] = 1
            else:
                ana2[y] = ana2.get(y) + 1
        return ana == ana2
