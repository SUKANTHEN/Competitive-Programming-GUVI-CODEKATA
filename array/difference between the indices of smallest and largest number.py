# Given a number N and array of N integers, print the difference between the indices of smallest and largest number(if there are multiple occurances, consider the first occurance).
# Input Size : |N| <= 1000000
# Sample Testcase :
# INPUT:
# 5
# 3 5 4 4 7
# OUTPUT:
# 4

n = int(input())
arr = [int(x) for x in input().split()]
minElem = arr[0]
maxElem = arr[0]
for i in range(1,len(arr)):
    if (arr[i] > maxElem):
        maxElem = arr[i]
    elif (arr[i] < minElem):
        minElem = arr[i]
#print(minElem,maxElem)
diff = abs(arr.index(minElem)-arr.index(maxElem))
print(diff)
