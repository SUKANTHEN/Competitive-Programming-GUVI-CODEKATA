# Q) Print the position of first 1 from right to left, in binary representation of an Integer.
# Sample Testcase :
# INPUT
# 18
# OUTPUT
# 2
"""
SOLUTION:
"""
n = int(input())
s = str(n)
val = s.find('1')
res = len(s)-int(val)
print(res)
