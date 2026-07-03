class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0
        j = len(heights)-1
        while i<j:
            h=min(heights[i],heights[j])
            l=j-i
            curarea=h*l
            if curarea>area:
                area = curarea
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1      
        return area