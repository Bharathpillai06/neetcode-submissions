class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
   
        y = len(numbers)-1
    
        for i in range(len(numbers)):
            while y > i:
                if(numbers[y]+numbers[i]==target):
                    return [i+1,y+1]
                else   :
                 y = y-1
            y = len(numbers)-1
