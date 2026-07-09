class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        lent = len(temperatures)
        for i in range(lent):
            counter = 0
            for j in range(i+1,lent):
                if max(temperatures[i+1:lent]) > temperatures[i]:
                    if temperatures[j]>temperatures[i]:
                        counter=j-i
                        break        
            output.append(counter)
        return output