# Q) Write a code to get a integer n as input and calculate the smallest perfect power of 2 greater than n.
# Sample Input :
# 48
# Sample Output :
# 64
'''
SOLUTION:
'''
n = int(input())
for i in range(100):
  if 2**i > n:
    print(2**i)
    break
