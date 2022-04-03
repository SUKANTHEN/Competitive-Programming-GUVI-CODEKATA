# Q) Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.
# INPUT
# 5 5
# OUTPUT
# yes
"""
SOLUTION:
"""
n,m = map(int,input().split(" "))
# This program can handle squared numbers till n,m value 99
squaredNums = [x**2 for x in range(100)]
if n*m in squaredNums:
    print("yes")
else:
    print("no")
