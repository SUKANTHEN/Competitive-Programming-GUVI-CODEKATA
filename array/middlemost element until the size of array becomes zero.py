# You are given with an array of numbers.You have to print the middlemost element until the size of array becomes zero. When n is odd print the (n/2)+1 index(indexing at 1)
# Sample Input :
# 5
# 1 2 3 4 5 
# Sample Output :
# 3 2 4 1 5
'''
SOLUTION:
'''
n = int(input())
arr = [int(x) for x in input().split()]
newLst = []
while (len(arr)>2):
  if len(arr)%2 != 0:
    midIndex = int(len(arr) // 2)
  else:
    midIndex = int(len(arr)//2)-1
  midElem = arr[midIndex]
  newLst.append(midElem)
  arr.pop(midIndex)

res = newLst + arr
print(*res)
