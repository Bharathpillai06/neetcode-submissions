class Solution:
    def isPalindrome(self, s: str) -> bool:
        y = 0
        z= len(s)-1
        while y<z:
            while y<z and not s[y].isalnum():
                y+=1
            while y<z and not s[z].isalnum():
                z-=1
            if s[y].lower() != s[z].lower():
                return False
            z-=1
            y+=1
        return True