class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while right > left:
            mid = (right + left) // 2

            total = 0
            for p in piles:
                total += math.ceil(p/mid)
            
            if total > h:
                left = mid + 1
            else:
                right = mid
        return right