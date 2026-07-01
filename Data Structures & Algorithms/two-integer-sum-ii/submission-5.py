class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 1
        while index1 < len(numbers):
            while index2 < len(numbers):
                if numbers[index1] + numbers[index2] == target:
                    return [index1 +1,index2+1]
                index2 += 1
            index1 +=1
            index2 = index1 +1
            