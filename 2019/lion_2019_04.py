'''
2019來恩盃:第 4 題 – 9 的倍數判別
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew
'''
n=int(input())
cnt=0
n9=n
if n9==9:
    cnt=1
while n9>10:
    x=0
    while n9>0:
        x+= n9%10
        n9//=10
    n9=x
    cnt+=1
if n9==9:
    print(f"Y {cnt}")
else:
    print("N")
'''
input:
999999999999999999999 
output:
Y 3

input:
9
output:
Y 1

input:
9999999999999999999999999999998
output:
N

input:
9765
output:
Y 2
'''
