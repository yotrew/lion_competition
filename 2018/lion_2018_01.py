'''
2018來恩盃:第 1 題 – 密文排列
同2020來恩盃:第 6 題 解密運算
Author:Yotrew Wing
https://github.com/yotrew

2022/10/10
解法:
表格解
'''
in_s=input().split(" ")
k=int(in_s[0])
p=in_s[1]
c=[[] for i in range(k)]
#print(p)
row=0
a=1 #往上或往下
for i in range(len(p)):
    print(p[i],row)
    c[row].append(p[i])
    row+=a
    if row==0 or row>=k-1: #反向
        a*=-1
out_str=""

print(c)
for i in c:
    out_str+="".join(i)
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
