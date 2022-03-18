# Q) Given a number N and an array of N elements, find the Bitwise XOR of the array elements.
# Sample Testcase :
# INPUT
# 2
# 2 4
# OUTPUT
# 6
'''
SOLUTION:
'''
def XOR_Calculator(arr):
    xorVal = 0
    for i in range(len(arr)):
        xorVal = xorVal ^ arr[i]
    return xorVal
    
n = int(input())
arr = [int(x) for x in input().split()]
res = XOR_Calculator(arr)
print(res)
