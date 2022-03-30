# Q) Given a number N and an array of N elements, find the Bitwise OR of the array elements.
# Input Size : N <= 100000
# Sample Testcase :
# INPUT
# 2
# 2 4
# OUTPUT
# 6
"""
SOLUTION:
"""
n = int(input())
nelem = list(map(int,input().split(" ")))
val = int(nelem[0])
for elem in nelem:
  val = val | elem
print(val)
