# Q) You are provided with a number ’n’. Your task is to tell whether that number is saturated. A saturated number is a number which is made by exactly two digits.
# Sample Input :
# 121
# Sample Output :
# Saturated
"""
SOLUTION:
"""
n = int(input())
n = str(n)
lst = []
for i in n:
    if i not in lst:
        lst.append(i)        
if len(lst) == 2:
    print('Saturated')
else:
    print('Unsaturated')
