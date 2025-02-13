#! python3
# minOper.py- Minimum Operations to Exceed Threshold Value II

num = [1,1,2,4,9]
k = 20

def minOperations(num, k):
    for i in num:
        if i > k:
            return 0
    operationsCount = 0
    while len(num) >= 2:
        num.sort()
        x = num[0]
        y = num[1]
        del num[0:2]
        newElem = x * 2 + y
        num.append(newElem)
        operationsCount = operationsCount + 1
        if newElem >= k:
            break
    if num[-1] < k:
        return -1
    return operationsCount
print(minOperations(num, k))
