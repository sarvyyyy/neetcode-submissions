class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_total = []
        i = 0
        j = k
        while j<=len(nums):
            window = nums[i:j]
            max_total.append(max(window))
            i+=1
            j+=1
        return max_total
