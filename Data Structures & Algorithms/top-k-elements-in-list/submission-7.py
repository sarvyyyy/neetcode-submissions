class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]]+=1
        final = []
        while k!=0:
            ans = 0
            maxi = float('-inf')
            for r,v in d.items():
                if v > maxi:
                    maxi = v
                    ans = r
            d[ans] = 0
            final.append(ans)
            k-=1
        return final
