class Solution:
    def minWindow(self, s: str, t: str) -> str:
        max_len=0
        i = 0
        j = len(t)
        sorted_t = sorted(t)
        while j<=len(s):
            window = s[i:j]
            p = i
            r = j
            while r<=len(s):
                window = s[p:r]
                counter = 0
                m = t
                temp_window = window
                for x in range(len(t)):
                    if t[x] in temp_window:
                        temp_window = temp_window.replace(t[x],"",1)
                        m = m.replace(t[x],"",1)
                if m == "":
                    return window
                p+=1
                r+=1
            j+=1
        return ""

