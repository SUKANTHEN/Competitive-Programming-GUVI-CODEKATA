# Q) You are given a large number made of only 0’s and 1’s.Your task is to find the max no of consecutive 1’s. If there are no 1’s print -1
# Sample Input :
# 101011111
# Sample Output :
# 5
'''
SOLUTION:
'''
n = int(input())
m = str(n)
count = 0
if '1' in m:
  for i in range(1,len(m)):
    if m[i-1] == m[i] == '1':
      count += 1
else:
  count = -1
if m[-1] == m[0] == '1':
  count += 1
print(count)
