'''
2018來恩盃:第 1 題 – 密文排列
同2020來恩盃:第 6 題 解密運算
Author:Yotrew Wing
https://github.com/yotrew

2022/10/10
解法:
找出規則
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
in_s=input().split(" ")
k=int(in_s[0])
c=in_s[1]
cl=len(c)
p=["" for i in range(cl)]
a=1 #往上或往下

i=0
for row in range(k):
    pos=row
    a=1
    while 0<=pos<cl:
        p[i]=c[pos]
        i+=1
        a*=-1
        if (row==0 or a==-1) and row!=k-1 : #第１列或其他列且向下
            pos+=(k-row-1)*2
        if (row==k-1 or a==1) and row!=0: #最後或其他列且向上
            pos+=row*2
            
        print(p)
       
out_str="".join(p)

print(out_str)

'''
input:
3 SAVEYOURSELF 

output:
SYSAEOREFVUL
#----------------------
input:
4 SOUTHERNTAIWAN

output:
SRAOENWNUHTITA

'''
