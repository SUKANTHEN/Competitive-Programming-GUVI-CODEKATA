#Given a number N and an array of N elements, every number is repeated except for one. Print that one number.
# Sample Testcase :
# INPUT
# 10
# 1 2 3 2 3 3 2 5 5 2
# OUTPUT
# 1
n = int(input())
arr = [int(x) for x in input().split()]
for i in arr:
    if arr.count(i) == 1:
        print(i)
        break
