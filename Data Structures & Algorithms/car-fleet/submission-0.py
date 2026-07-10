class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            time_needed = (target-position[i])/speed[i]
            cars.append([position[i],time_needed])

        cars.sort(key = lambda x: x[0], reverse = "True")
        stack = []
        for pos,time in cars:
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        
        return len(stack)