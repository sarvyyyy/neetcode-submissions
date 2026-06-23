class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        r=""
        for i in s:
            if i.isalnum():
                r+=i
        
        if r == r[::-1]:
            return True
        else:
            return False