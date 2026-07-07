class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = len(s1)
        sorted_s1 = sorted(s1)
        while j<=len(s2):
            window = s2[i:j]
            if sorted(window)==sorted_s1:
                return True
            j+=1
            i+=1
        return False