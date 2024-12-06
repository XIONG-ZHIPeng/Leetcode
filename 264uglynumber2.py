class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        un = set([2,3,5])
        products = set([2,3,5])
        count = 1

        while count != n:


            next_u = min(un)
            un.remove(next_u)
            for product in products:
                element = product * next_u
                if element not in un:
                    un.add(element)
            count += 1
        return next_u

        

        