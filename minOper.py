#! python3
# minOper.py- Minimum Operations to Exceed Threshold Value II

num = [2, 4, 11, 10, 1, 3]
k = 20
operationsCount = 0
def minOperations(num, k):
    for i in num:
        if i > k:
            return 0
    
    while len(num) >= 2:
        x = min(num)
        del num[x.index()]
        y = min(num)
        del num[y.index()]
        newElem = x * 2 + y
        num.append(newElem)
        operationsCount = operationsCount + 1
        if newElem >= k:
            break
    if num[-1] < k:
        return -1
    return operationsCount
