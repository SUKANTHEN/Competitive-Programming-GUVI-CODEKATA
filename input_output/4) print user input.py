#Sample Input :
# 2 4
# 2 4
# 2 4
#Sample Output :
# 2 4
# 2 4
# 2 4

# SOLUTION:
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
arr3 = [int(x) for x in input().split()]
print(*arr1)
print(*arr2)
print(*arr3)
