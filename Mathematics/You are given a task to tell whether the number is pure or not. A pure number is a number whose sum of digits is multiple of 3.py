# Q) You are given a task to tell whether the number is pure or not. A pure number is a number whose sum of digits is multiple of 3.
# Sample Input :
# 13
# Sample Output :
# not
"""
SOLUTION:
"""
n = int(input())
s = str(n)
sumVal = 0
for num in s:
    sumVal += int(num)   
if (sumVal >= 3) and (sumVal % 3 == 0):
    print("yes")
else:
    print("not")
