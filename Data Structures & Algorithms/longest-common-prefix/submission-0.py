class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """longest = strs[0]
        for i in range(1,len(strs)):
            for x in range(min(len(longest),len(strs[i]))):
                if longest[x] != strs[x]:
                    longest = longest[:x]
        return longest"""
        longest = strs[0]
        count = 0
        for x in range(len(strs)):
            for y in range(len(longest)):
                if(y > len(strs[x])-1 or longest[y] != strs[x][y]):
                    longest = longest[0:count]
                    break
                else:
                    count+=1
            count = 0
        return longest
