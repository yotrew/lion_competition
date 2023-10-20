'''
2020來恩盃:第 6 題 解密運算
2018來恩盃:第 1 題 – 密文排列的反向解--演算法相同，只要對調明文與密文的分配
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew

解法:
找出規則後反推
如:
3 123456789
1   5   9
 2 4 6 8
  3   7

4 123456789...
1     7      #第0列每次都是加上(k-0)*2 <-- 7-1=6
 2   6 8     #第1列向下同第0列，都是加上(k-1)*2 <-- 6-2=4，向上同最後1列，row號*2 <--8-6=2
  3 5   9    #第2列向下同第0列，都是加上(k-2)*2 <-- 5-3=2，向上同最後1列，row號*2 <--9-5=4
   4     10  #最後1列row號*2 <--10-4=6
'''

k=int(input())
p=input()
pl=len(p)
c=["" for i in range(pl)]

#print(p)
i=0
a=1 #往上或往下
for row in range(k): #列數，一列一列處理
    pos=row
    a=1
    while 0<=pos<pl:
        c[pos]=p[i] #<--解密，加密-->p[i]=c[pos]
        i+=1
        a*=-1
        if (row==0 or a==-1) and row!=k-1 : #第１列或其他列且向下
            pos+=(k-row-1)*2
        if (row==k-1 or a==1) and row!=0: #最後或其他列且向上
            pos+=row*2
        
print("".join(c))

'''
input:
3
uetnvriyis

output:
university
#----------------------
input:
2
uiestnvriy

output:
university
#----------------------
input:
3
sysaeorefvul 

output:
saveyourself
#----------------------
input:
2
cmueoptr

output:
computer
#----------------------
'''
