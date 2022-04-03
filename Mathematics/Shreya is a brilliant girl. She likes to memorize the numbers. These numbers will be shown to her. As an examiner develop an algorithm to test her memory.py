# Q) Shreya is a brilliant girl. She likes to memorize the numbers. These numbers will be shown to her. As an examiner develop an algorithm to test her memory.
#Sample Input :
# 10
# 1 1 1 2 2 2 3 8 9 7
# 5
# 1 2 3 0 5
# Sample Output :
#3 3 1 Not Present Not Present
"""
SOLUTION:
"""
y = int(input())
n = list(map(int,input().split()))
t = int(input())
T = list(map(int,input().split()))
notPresent = "Not Present"
lst = []
for i in T:
    if (i in n) and (i not in lst):
        lst.append(str(n.count(i)))
    else:
        lst.append(notPresent)
print(" ".join(lst))
