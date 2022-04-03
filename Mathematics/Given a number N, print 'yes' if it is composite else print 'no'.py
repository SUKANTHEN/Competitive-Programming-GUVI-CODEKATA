# Q) Given a number N, print 'yes' if it is composite else print 'no'.
# INPUT
# 123
# OUTPUT
# yes
"""
SOLUTION:
"""
N = int(input())
flag = 'no'
for i in range(2, int(N/2)+1):
  if N % i == 0:
    flag = 'yes'
print(flag)
