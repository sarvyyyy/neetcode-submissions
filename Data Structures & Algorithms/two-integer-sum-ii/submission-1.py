class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        last = n-1
        first = 0
        for i in range(n):
            if numbers[first]+numbers[last]>target:
                last-=1
            elif numbers[first]+numbers[last]<target:
                first+=1
        return [first+1,last+1]