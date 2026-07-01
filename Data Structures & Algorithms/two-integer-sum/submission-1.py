class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dick = dict()
        count = 0
        lis = []
        for x in nums: 
            if(target-x in dick):
                return [dick.get(target-x), count]
            else:
                dick[x] = count
            count += 1
            
            
