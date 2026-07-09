class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)
        """
        
        k = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k