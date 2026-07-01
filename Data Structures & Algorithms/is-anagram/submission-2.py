class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        my_dict = {}

        for i in s:
            my_dict[i]=  my_dict.get(i, 0) + 1
        for i in t:
            my_dict[i] = my_dict.get(i, 0) - 1
            if my_dict[i] == -1:
                return False
        for i in my_dict:
            if my_dict[i] != 0:
                return False
        return True
        

            

