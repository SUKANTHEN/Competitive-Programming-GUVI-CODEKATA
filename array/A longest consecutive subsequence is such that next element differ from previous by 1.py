#You are given an array.Your task is to print the length of longest consecutive subsequence. A longest consecutive subsequence is such that next element differ from previous by 1.
# Sample Input :
# 8
# 1 6 5 3 2 4 10 12
# Sample Output :
# 6
'''
SOLUTION:
'''
n = int(input())
arr = [int(x) for x in input().split()]
sortedArr = sorted(arr)
sublist = [sortedArr[0]]
for i in range(0,len(sortedArr)):
    if sortedArr[i] - sortedArr[i-1] == 1:
        sublist.append(sortedArr[i])
        
print(len(sublist))
