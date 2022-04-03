# Q) You are given a number ‘n’. You have to tell whether a number is great or not. A great number is a number whose sum of digits let (m) and product of digits let(j) when summed together gives the number back
# Sample Input :
# 59
# Sample Output :
# Great
"""
SOLUTION:
"""
n = int(input())
m = str(n)
summer = 0
for i in m:
    summer = summer + int(i)
    
mul = 1
for i in range(1,len(m)+1):
    mul = mul * int(m[i-1])

if mul + summer == n:
    print('Great')
else:
    print('no')
