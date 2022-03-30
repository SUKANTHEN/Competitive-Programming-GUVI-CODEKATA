# Q) Given an array of N elements switch(swap) the element with the adjacent element and print the output.
# Sample Testcase :
# INPUT
# 5
# 3 2 1 2 3
# OUTPUT
# 2 3 2 1 3
"""
SOLUTION:
"""
n = int(input())
l = list(map(int,input().split()))
if n % 2 != 0:
  for i in range(0, n-1, 2):
    temp = l[i]
    l[i] = l[i+1]
    l[i+1] = temp
else:
  for i in range(0, n, 2):
    temp = l[i]
    l[i] = l[i+1]
    l[i+1] = temp
l = list(map(str,l))
print(" ".join(l))
