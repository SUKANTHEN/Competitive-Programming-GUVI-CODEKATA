# Given a number N and an array of N strings, find the number of strings that are an anagram of 'kabali'.If there exists no anagram for the given string print '0'.
# Input Size : 1 <= N <= 1000

#Sample Testcase :
# INPUT:
# 5
# kabali
# kaabli
# kababa
# kab
# kabail

# OUTPUT:
# 3
'''
SOLUTION:
'''
def anagramChecker(word,testString):
    flag = False
    lst = [i for i in str(word)]
    lst = sorted(set(lst))
    lstTest = [i for i in str(testString)]
    lstTest = sorted(set(lstTest))
    #print(lst,lstTest)
    if (lst == lstTest) and (len(word) == len(testString)):
        flag = True
    return flag
    
s  = int(input())
arr = []
for i in range(s):
  arr.append(input())
testString = "kabali"
count = 0
for word in arr:
    if anagramChecker(word,testString) == True:
        count +=1        
print(count)
