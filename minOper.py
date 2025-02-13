#! python3
# minOper.py- Minimum Operations to Exceed Threshold Value II

num = [2,11,10,1,3]
k = 10

def minOperations(num, k):
    if all( i >= k for i in num):
        return 0
    operationsCount = 0
    while len(num) >= 2 and if not all( i >= k for i in num):
        num.sort()
        x = num[0]
        y = num[1]
        del num[0:2]
        newElem = x * 2 + y
        num.append(newElem)
        operationsCount = operationsCount + 1

    if num[-1] < k:
        return -1
    return operationsCount
print(minOperations(num, k))
