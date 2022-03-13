# Given a number N and an array of N integers, print the minimum sum of the sub-array from the given array.
# Sample Testcase :
# INPUT
# 4
# 2 4 4 2
# OUTPUT
# 2
'''
SOLUTION:
'''
def smallestSubArray(arr):
    minEnd = arr[0]
    minCurr = arr[0]
    for i in range(1,len(arr)):
        if (minEnd > 0):
            minEnd = arr[i]
        else:
            minEnd += arr[i]
        minCurr = min(minCurr,minEnd)
    return minCurr
    
n = int(input())
arr = [int(x) for x in input().split()]
val = smallestSubArray(arr)
print(val)
