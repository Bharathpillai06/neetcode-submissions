class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        
        """
        ret = 0
        for i in range(len(nums)):
            ret += nums[i] ^ i
        return ret
        """
        
        """
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res"""


        n = len(nums)
        for i in range(len(nums)):
            n ^= i ^ nums[i]
        return n