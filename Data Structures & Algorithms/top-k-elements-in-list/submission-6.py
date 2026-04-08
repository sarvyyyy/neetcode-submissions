class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        bucket = []
        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            temp = [nums[i],1]
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    temp[1]+=1
            bucket.append(temp)
        output = []
        while k!=0:
            best = [0,0]
            for m in range(len(bucket)):
                if bucket[m][1]>best[1]:
                    best[1] = bucket[m][1]
                    best[0] = bucket[m][0]
            output.append(best[0])
            bucket.remove(best)
            k-=1
        return output