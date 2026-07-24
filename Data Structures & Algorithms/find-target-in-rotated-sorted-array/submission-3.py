class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rot = 0
        n = len(nums)
        temp = nums
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                temp = nums[i:] + nums[0:i]
                rot = i
                break
        left = 0
        right = n-1
        while left<=right:
            mid = (left + right) // 2
            if temp[mid] == target:
                return (mid+rot) % n
            elif temp[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1