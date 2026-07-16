class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        for i in range(n):
            stack = []
            area = 0
            h = heights[i]
            if i>0 and i!=n-1:
                left_window = heights[0:i]
                left_window.reverse()
                right_window = heights[i+1:n]
                for j in left_window:
                    if j>=h:
                        stack.append(j)
                    else:
                        break
                for k in right_window:
                    if k>=h:
                        stack.append(k)
                    else:
                        break
                area = h*(len(stack)+1)
                if area>max_area:
                    max_area = area  
            elif i == 0:
                right_window = heights[1:n]
                for x in right_window:
                    if x>=h:
                        stack.append(x)
                    else:
                        break
                area = h*(len(stack)+1)
                if area>max_area:
                    max_area = area
            elif i == n-1:
                left_window = heights[0:n-1]
                left_window.reverse()
                for y in left_window:
                    if y>=h:
                        stack.append(y)
                    else:
                        break
                area = h*(len(stack)+1)
                if area>max_area:
                    max_area = area
        return max_area
