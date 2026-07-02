class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        li = []
        for i in range(len(nums)):
            li.append(nums[i])        
        return li + li