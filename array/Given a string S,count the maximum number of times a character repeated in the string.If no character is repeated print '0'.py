# Given a string S,count the maximum number of times a character repeated in the string.If no character is repeated print '0'.
# Input Size : 1 <= N <= 100000
# Sample Testcase :
# INPUT
# codekata
# OUTPUT
# 2
'''
SOLUTION:
'''
S = input()
maxi = 0
for i in range(0,len(S)):
    if S.count(S[i]) > maxi:
        maxi = S.count(S[i])
print(maxi)
