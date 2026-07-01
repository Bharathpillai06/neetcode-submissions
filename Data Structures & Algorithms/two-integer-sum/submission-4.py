class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bums= {}
        for y in range(len(nums)):
            
            if target - nums[y] in bums:
                return [bums.get(target - nums[y]), y]
            bums[nums[y]] = y
        return False