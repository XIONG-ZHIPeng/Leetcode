import heapq
class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        ratio = [ (((item[0]/item[1]) - (item[0]+1)/(item[1]+1)), index) for index, item in enumerate(classes)]
        heapq.heapify(ratio)
        for _ in range(extraStudents):
            item = heapq.heappop(ratio)
            index = item[1]
            classes[index] = [classes[index][0]+1, classes[index][1]+1]
            new_item = (((classes[index][0]/classes[index][1]) - ((classes[index][0]+1)/(classes[index][1]+1))),index)
            heapq.heappush(ratio,new_item)
        
        length = len(classes)
        result = 0
        for x, y in classes:
            result += x/y
        return format(result/length, '.5f')

classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
s = Solution()
print(s.maxAverageRatio(classes, extraStudents)) # 0.78333