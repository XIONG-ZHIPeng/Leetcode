import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1
        un = set(primes)
        p = deepcopy(primes)
        heapq.heapify(p)
        for i in range(1,n):
            next_u = heapq.heappop(p)
            for prime in primes:
                element = prime * next_u
                if element not in un:
                    un.add(element)
                    heapq.heappush(p, element)



        return next_u


            
        

        