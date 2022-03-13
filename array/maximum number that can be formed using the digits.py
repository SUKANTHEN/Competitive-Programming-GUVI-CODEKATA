# A number is given as input.Find the maximum number that can be formed using the digits.
#Input Size : N <= 10000000
# Sample Testcase :
# INPUT
# 4123
# OUTPUT
# 4321
'''
SOLUTION:
'''
n = int(input())
s = str(n)
arr = [i for i in s]
arr = list(map(int,arr))
sortedArr = sorted(arr,reverse = True)
sortedArr = list(map(str,sortedArr))
print("".join(sortedArr))
