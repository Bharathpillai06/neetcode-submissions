class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for x in range(len(temperatures)):
            for y in range(x,len(temperatures)):
                if temperatures[y] > temperatures[x]:
                    ans.append(y-x)
                    break
            else:
                ans.append(0)
        return ans