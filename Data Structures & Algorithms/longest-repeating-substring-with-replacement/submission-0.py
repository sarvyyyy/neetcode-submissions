class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=0
        max_len = 0 
        while j<len(s):
            window = s[i:j+1]
            winlen = len(window)
            
            max_freq=0
            for char in set(window):
                char_count = window.count(char)
                if char_count > max_freq:
                    max_freq = char_count

            garbage = winlen - max_freq

            if garbage<=k:
                if max_len<winlen:
                    max_len = winlen
                j+=1
            else:
                i+=1
        return max_len


