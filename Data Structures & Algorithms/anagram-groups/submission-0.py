class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        x ={}
        y = []

        for i in strs:

            sorted_s_tuple = tuple(sorted(i))
            if sorted_s_tuple in x:
                x[sorted_s_tuple].append(i)
            else:
                x[sorted_s_tuple] = [i]

        for value in x.values():
            y.append(value)
                   
        return y