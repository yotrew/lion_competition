'''
2020來恩盃:第 2 題 位移加密法
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew
'''
p=input()
key=int(input())
#print(p)
for i in p:
    c=chr( ( (ord(i)-65 + key)%26 ) + 65 )
    print(c,end="")
print()
'''
input:
SECURE
7
output:
ZLJBYL

input:
HACKING
12

output:
TMOWUZS
'''
