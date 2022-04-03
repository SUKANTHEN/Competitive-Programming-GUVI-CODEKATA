# Q) Assume your brother studies in class 2. He has to  complete his homework on co-primes. As an elder sibling help him in finding whether the given two numbers is co-prime or not.
# Sample Input :
# 3 5
# Sample Output :
# 1
"""
SOLUTION:
"""
n,m = map(int,input().split())
flag = 1
for i in range(2,int(n//2+1)):
    if n%i == 0 and m%i == 0:
        flag = 0
        break
print(flag)
