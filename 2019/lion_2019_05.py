'''
2019來恩盃:第 5 題 – 超長整數加總之檢查碼計算
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew

'''
a=int(input())
b=int(input())
c=a+b
s=0
while c>0:
    s+=c%10
    c//=10
print(s)
'''
input:
123
456
output:
21

input:
123456789012345
123456789012345
output:

'''
