class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in range(len(s)):
            if s[i].isalnum():
                st += s[i].lower()
        x = len(st)
        y = 0
        z= x-1
        while y<z:
            if st[y] == st[z]:
                y+=1
                z-=1
            else:
                return False
        return True

        