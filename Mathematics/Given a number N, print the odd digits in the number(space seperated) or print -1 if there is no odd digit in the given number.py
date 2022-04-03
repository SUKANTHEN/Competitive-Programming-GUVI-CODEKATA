# Q) Given a number N, print the odd digits in the number(space seperated) or print -1 if there is no odd digit in the given number.
# INPUT
# 2143
# OUTPUT
# 1 3
"""
Solution
"""
N = input()
lst = []
for i in N:
    if int(i)%2 != 0:
        lst.append(str(i))
if len(lst) == 0:
    print(-1)
else:
    print(" ".join(lst))
