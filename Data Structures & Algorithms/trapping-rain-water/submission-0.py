class Solution:
    def trap(self, height: List[int]) -> int:
        j=1
        total = 0
        while j<len(height)-1:
            max_left = 0
            max_right = 0
            for l in range(0,j):
                if height[l]>max_left:
                    max_left = height[l]
            for r in range(j+1,len(height)):
                if max_right<height[r]:
                    max_right = height[r]
            water_level = min(max_left, max_right)
            trapped = water_level - height[j]
            if trapped>0:
                total+=trapped
            j+=1
            
        return total
            
            
            
