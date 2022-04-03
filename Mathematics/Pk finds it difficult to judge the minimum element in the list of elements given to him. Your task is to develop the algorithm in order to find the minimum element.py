# Q) Pk finds it difficult to judge the minimum element in the list of elements given to him. Your task is to develop the algorithm in order to find the minimum element.
# Sample Input :
# 5
# 3 4 9 1 6
# Sample Output :
# 1
"""
SOLUTION:
"""
def minFinder(arr):
    minVal = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < minVal:
            minVal = arr[i]
    return minVal
            
n = int(input())
arr = list(map(int,input().split()))
val = minFinder(arr)
print(val)
