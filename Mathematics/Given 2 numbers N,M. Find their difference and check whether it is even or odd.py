# Q) Given 2 numbers N,M. Find their difference and check whether it is even or odd.
# INPUT
# 5 5
# OUTPUT
# even
"""
SOLUTION:
"""
n,m = map(int,input().split())
val = abs(n-m)
if val % 2 == 0:
    print("even")
else:
    print("odd")
