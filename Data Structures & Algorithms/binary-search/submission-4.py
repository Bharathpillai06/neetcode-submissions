class Solution:
    def search(self, nums: List[int], target: int) -> int:


        




        
        """for i in nums:
            if (i == target):
                return (nums.index(i))
        return -1    
       """
       
       
       
       
        
        numz = len(nums)//2
        maxi = len(nums)
        mini = 0

        while True:   
            if target == nums[numz]:
                break
            elif target > nums[numz]:
                mini = numz
                numz = (mini + maxi) //2
            elif target < nums[numz]:
                maxi = numz
                numz = (mini + maxi) //2
            if maxi == numz or mini == numz and target != nums[numz]:
                return -1
        return numz
        