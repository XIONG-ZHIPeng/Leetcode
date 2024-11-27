class Solution:
    def findChampion(self, n, edges):
        champion = -1
        stronger = set()
        weaker = set()

        for item in edges:
            if item[1] not in weaker:
                weaker.add(item[1])
            if item[1] in stronger:     
                stronger.remove(item[1])
            if item[0] in weaker and item[0] in stronger:
                stronger.remove(item[0])
            elif item[0] not in stronger:
                stronger.add(item[0])

        if len(stronger) == 1:
            champion = stronger.pop()
        stronger.add(champion)

        for i in range(n):
            if i not in weaker and i not in stronger:
                champion = -1
                break
        
        return champion
    
s = Solution()
print(s.findChampion(3,[[0,2],[1,0]]))