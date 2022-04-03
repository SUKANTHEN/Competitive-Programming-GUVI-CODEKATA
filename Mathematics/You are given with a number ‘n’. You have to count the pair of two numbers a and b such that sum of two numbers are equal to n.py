# Q) You are given with a number ‘n’. You have to count the pair of two numbers a and b such that sum of two numbers are equal to n.
# Sample Input :
# 5
# Sample Output :
# 4
"""
SOLUTION:
"""
n = int(input())
myset = set()
for i in range(n):
    for j in range(n):
        if i + j == n:
            myset.add((i,j))
            
print(len(myset))       
