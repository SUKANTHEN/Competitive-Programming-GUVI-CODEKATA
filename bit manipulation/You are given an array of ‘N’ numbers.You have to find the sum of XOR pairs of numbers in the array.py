# Q) You are given an array of ‘N’ numbers.You have to find the sum of XOR pairs of numbers in the array.
# Sample Input :
# 3
# 7 3 5
# Sample Output :
# 12
'''
SOLUTION:
'''
def XORSummer(arr):
    res = 0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            res = res + (arr[i] ^ arr[j])
    return res
    
n = int(input())
arr = [int(x) for x in input().split()]
val = XORSummer(arr)
print(val)
