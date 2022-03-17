# Vasanth is working at GUVI. He has been taking leave often in the past couple of weeks and his manager, who also happens to be his friend, is worried that Vasanth might be exceeding his number of paid holidays, which might be a black mark in Vasanth monthly report. The manager analysis Vasanth’s attendance register and decides to warn him beforehand. The attendance register has a ‘P’ marked for present and an ‘A’ marked for absent. Vasanth will be blacklisted if his attendance falls below 25%. Your task is to help the manager find out whether Vasanth could be blacklisted or not.
# Sample Input :
# 5
# P P A A A
# Sample Output :
# Not Blacklisted
'''
SOLUTION:
'''
def AttendancePercentage(arr):
    if 'P' in arr:
        presentCount = arr.count('P')
        totalAttendance = (presentCount/len(arr))*100
    else:
        totalAttendance = 0
    if totalAttendance <= 25:
        return 'Blacklisted'
    else:
        return 'Not Blacklisted'

n = int(input())
s = input()
arr = s.split(" ")
res = AttendancePercentage(arr)
print(res)
