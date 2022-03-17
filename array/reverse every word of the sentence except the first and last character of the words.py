#Given a string S consisting of a sentence, the task is to reverse every word of the sentence except the first and last character of the words.
# Sample Testcase :
# INPUT
# guvi coding platform
# OUTPUT
# gvui cnidog proftalm.
'''
SOLUTION:
'''
s = input()
arr = s.split(" ")
lst = []
for i in arr:
    if len(i) > 3:
        startLetter = i[0]
        endingLetter = i[len(i)-1]
        revString = (i[1:len(i)-1])[::-1]
        newChar = startLetter + revString + endingLetter 
        lst.append(newChar)
    else:
        lst.append(i)
print(*lst)
