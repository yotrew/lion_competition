'''
2020來恩盃:第 1 題 三角波波形
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew

把波形分成2半來做處理
'''
b=int(input())
a=int(input())
for i in range(a):
    for j in range(1,b+1):
        print(f"{j}"*j)
    for j in range(b-1,0,-1):
        print(f"{j}"*j)

    if i!=a-1: #最後一次不印空白列(要以測驗系統為主:看會不會對最後一列最檢測)
        print()
'''
input:
1
1
output:
1

input:
3
1
output:
1
22
333
22
1
input:
2
3
output:
1
22
1

1
22
1

1
22
1
'''
