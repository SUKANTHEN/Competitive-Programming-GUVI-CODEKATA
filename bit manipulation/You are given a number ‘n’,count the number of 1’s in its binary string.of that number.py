# Q) You are given a number ānā,count the number of 1ās in its binary string.of that number
# Sample Input :
# 4
# Sample Output :
# 1
'''
SOLUTION:
'''
n = int(input())
s = str(bin(n)).count("1")
print(s)
