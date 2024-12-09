class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        length = len(piles)
        piles.sort()
        l, r, consume = 1, max(piles), 0
        k = int((l + r) / 2)
        while l < r:
            consume = 0
            for num in piles:   
                consume += int(num / k)
                if num % k != 0:
                    consume += 1
            if consume == h:
                return k
            elif consume > h:
                l, k = k + 1, int((k + r)/2)
            elif consume < h:
                r, k = k - 1, int((l + k) / 2)
        return int((l+r)/2)
        

        