# Q) Given a number N and an array of N elements, print all elements lesser than N in descending order.If no element found print -1
# INPUT
# 5
# 2 14 15 14 3
# OUTPUT
# 3 2
'''
SOLUTION:
'''
def findLesserNumbers(arr,n):
    lst = [i for i in arr if i<n]
    lst = sorted(lst,reverse=True)
    return lst
    
n = int(input())
arr = list(map(int,input().split()))
if len(arr)>1:
    val = findLesserNumbers(arr,n)
    if len(val)>=1:
      print(*val)
    else:
      print(-1)
else:
    print(-1)
