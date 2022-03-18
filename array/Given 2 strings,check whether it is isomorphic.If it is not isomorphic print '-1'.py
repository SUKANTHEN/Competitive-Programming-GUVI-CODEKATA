# Q) Given 2 strings,check whether it is isomorphic.If it is not isomorphic print '-1'.
# Input Size : |s| <= 100000(complexity O(nlogn))
# Sample Testcase :
# INPUT
# aab xxy
# OUTPUT
# yes
'''
SOLUTION:
'''
def basevalueConvertor(s):
  dic = {}
  res = ""
  val = 0
  for i in range(len(s)):
    if s[i] not in dic:
      dic[s[i]] = val
      val += 1
  for i in s:
    if i in dic.keys():
      res += str(dic[i])
  return res
  
s1,s2 = map(str,input().split())
if len(s1) == len(s2):
    val_s1 = basevalueConvertor(s1)
    val_s2 = basevalueConvertor(s2)
    if val_s1 == val_s2:
        print("yes")
    else:
        print("no")
else:
    print("no")
