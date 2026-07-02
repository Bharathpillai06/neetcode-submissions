class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count  = 0
        for x in nums:
            count ^= x
        return count