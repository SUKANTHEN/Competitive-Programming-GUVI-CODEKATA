# Q) You are given a number ‘n’ and a bit ‘K’,your task is to tell whether the first bit is 1. Return true or false according to the scenario. First bit starts from right.(0 based indexing)
# Sample Input :
# 4
# 0
# Sample Output :
# False
'''
SOLUTION:
'''
n = int(input())
k = int(input())
binaryval = bin(n)
val = binaryval[2:]
lenVal = len(val)
if val[(lenVal-1)-k] == "1":
    print("true")
else:
    print("False")
