# Q) You are given an array of non-negative integers representing height of walls at index i as Ai and the width of each block is 1. Compute how much air can be encapsulated between the walls of chamber.
# Sample Input :
# 3
# 7 4 9
# Sample Output :
# 3
"""
SOLUTION:
"""
n = int(input())
arr = [int(x) for x in input().split()]
min = arr[0]
for i in range(1,len(arr)):
  if (abs(arr[i-1]- arr[i])) < min:
    min = (abs(arr[i-1]- arr[i]))
print(min)
