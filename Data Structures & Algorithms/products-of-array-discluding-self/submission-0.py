class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        for i in range(len(nums)):
            for y in range(len(nums)):
                if i!= y:
                    result[i] *= nums[y]
        return result
        