class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        j = 0
        max_len = 0
        while j<len(s):
            if s[j] not in s[i:j]:
                j+=1
            else:
                i+=1
            if j-i>max_len:
                max_len = j-i 
        return max_len 
