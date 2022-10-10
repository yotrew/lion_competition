'''
2020來恩盃:第 4 題 – 資料傳輸編碼
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew

解法:
按題目解釋,建表後先排序,排序後一次切一半
因此使用2元搜尋法切
'''

def binary_cut(prefix,l,r):
    global table
    
    if l>=r :
        table[l][2]=prefix
    else:
        #print(prefix,l,r)
        binary_cut(prefix+"0",l,(r-l+1)//2-1)
        binary_cut(prefix+"1",l+(r-l+1)//2,r)
        #print(prefix+"1:",(r-l+1)//2,r)


n=int(input())
data=list(input().split(" "))
prob=list(map(float,input().split(" ")))
table=[]

if sum(prob)>1:
    print(-1)
else:
    
    for i in range(len(data)):
        table.append([data[i],prob[i],""])
    #print(table)
    table.sort(key=lambda x:x[1],reverse=True)
    binary_cut("",0,len(table)-1)
for i in table:
    print(f"{i[0]}:{i[2]}")
#print(table)
'''
input:
5
A B C D E
0.22 0.28 0.15 0.30 0.05

output:
D：00
B：01
A：10
C：110
E：111


input:
3
a1 a2 a3
0.1 0.88 0.02

output:
a2：0
a1：10
a3：11

input:
3
a1 a2 a3
0.1 0.9 0.2


output:
-1
'''
