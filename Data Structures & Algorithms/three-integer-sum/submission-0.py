class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        total = []
        nums.sort()
        for i in range(len(nums)):
            j = 0
            k = len(nums)-1
            while j<k:
                if j==i:
                    j+=1
                    continue
                if k==i:
                    k-=1
                    continue
                target = nums[i]
                cursum = -(nums[j]+nums[k])
                if cursum==(target):
                    triplet = sorted(([nums[i],nums[j],nums[k]]))
                    if triplet not in total:
                        total.append(triplet)
                    j+=1
                    k-=1
                if cursum>target:
                    j+=1
                if cursum<target:
                    k-=1
        return total

