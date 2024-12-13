import heapq
import math

class Solution:
    def pickGifts(self, gifts, k):
        gifts = [- num for num in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            max_pile = heapq.heappop(gifts)
            new_one = - int(math.sqrt(-max_pile))
            heapq.heappush(gifts, new_one)
        return - sum(gifts)
        
        