#! python3
# minOper.py- Minimum Operations to Exceed Threshold Value II

num = [2, 4, 11, 10, 1, 3]
k = 10
def minOperations(num, k):
    for i in num:
        if i > k:
            return 0
    while len(num) >= 2:
        

