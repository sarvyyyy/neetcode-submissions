class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp = []
            if nums[i]<nums[i-1]:
                temp = nums[i:] + nums[0:i]
                nums = temp
                break
        return nums[0]
        

            
                