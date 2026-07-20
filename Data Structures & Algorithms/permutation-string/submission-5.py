class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = sorted(s1)
        z = len(s1)
        
        
        for i in range(len(s2) - z + 1):
            substring_sorted = sorted(s2[i : i + z])
            
            if substring_sorted == target:
                return True
                
        return False