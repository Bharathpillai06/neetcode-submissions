class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        nums.sort()
        ans = set()
        i = 0
        while i < len(nums):
            k = i + 1
            j = len(nums) - 1
            while k < j:
                total = nums[i] + nums[k] + nums[j]
                if total == 0:
                    ans.add((nums[i], nums[k], nums[j]))
                    k += 1
                    j -= 1
                elif total < 0:
                    k += 1
                else:
                    j -= 1
            i += 1
        return list(ans)
        
        """res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res"""