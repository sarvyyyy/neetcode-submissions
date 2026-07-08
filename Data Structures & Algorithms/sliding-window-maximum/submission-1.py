class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_total = []
        i = 0
        j = k
        while j<=len(nums):
            window = nums[i:j]
            max_element = float("-inf")
            for k in window:
                if k > max_element:
                    max_element = k
            max_total.append(max_element)
            i+=1
            j+=1
        return max_total
