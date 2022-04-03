# Q) You are given an array of numbers. Print the least occurring element. If there is more than 1 element print all of them in decreasing order of their value.
# Sample Input :
# 9
# 1 6 4 56 56 56 6 4 2
# Sample Output :
# 2 1
"""
SOLUTION:
"""
def minCount_Identifier(arr):
    minCount = 1
    setArr = set(arr)
    for i in setArr:
        if arr.count(i) < minCount:
            minCount = arr.count(i)
    return minCount
    
n = int(input())
arr = [int(x) for x in input().split()]
minCount = minCount_Identifier(arr)
lst = [i for i in arr if arr.count(i)==minCount]
lst = sorted(lst,reverse=True)
print(*lst)
