# Given 2 numbers N and K.Print the number of occurrences of K in N.If K is not found print '-1'.
# Input Size : 1 <= N <= 100000, 0 <= K <= 9
#Sample Testcase :
#INPUT:
# 1000 0
#OUTPUT:
# 3

'''
SOLUTION:
'''
n,k = map(int,input().split())
s = str(n)
countN = -1
if str(k) in s:
    countN = s.count(str(k))
print(countN)
