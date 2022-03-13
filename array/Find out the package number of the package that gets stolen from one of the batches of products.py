# Ram is a marketing manager at GUVI. He observes that for every two batches of products, one package is extra in one of the batches. He realises that someone is stealing the package from the other batch. He decides to document the discovery so as to report to his superior. Find out the package number of the package that gets stolen from one of the batches of products.
#Sample Input :
#2
#7
#2 4 6 8 9 10 12
#2 4 6 8 10 12
#6
#3 5 7 9 11 13
#3 5 7 11 13
#Sample Output :
#4
#3
'''
SOLUTION:
'''
def missingElemIndex(arr1,arr2):
    if len(arr1) >= len(arr2):
        largestArr,smallestArr = arr1,arr2
    elif len(arr1) < len(arr2):
        largestArr,smallestArr = arr2,arr1
    val = [i for i in range(0,len(largestArr)) if not largestArr[i] in smallestArr]
    if len(val)>0:
        return val[0]
    else:
        return -1

testCases = int(input())
for i in range(testCases):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    res = missingElemIndex(arr1,arr2)
    print(res)
