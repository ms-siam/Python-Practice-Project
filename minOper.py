#! python3
# minOper.py- Minimum Operations to Exceed Threshold Value II

num = [2,11,10,1,3]
k = 10
import bisect
class Solution:
    def minOperations(num, k):
        num.sort()
        if all( i >= k for i in num):
            return 0
        operationsCount = 0
        while len(num) >= 2 and not all( i >= k for i in num):
            
            x = num.pop(0)
            y = num.pop(0)
            
            newElem = x * 2 + y
            bisect.insort(num, newElem)
            operationsCount = operationsCount + 1

        if num[-1] < k:
            return -1
        return operationsCount
Solution().minOperations(nums, k)  

