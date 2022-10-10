'''
2020來恩盃:第 6 題 解密運算
同2018來恩盃:第 1 題 – 密文排列
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew

解法:
表格解
'''

k=int(input())
p=input()
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
3
university

output:
uetnvriyis
#----------------------
input:
2
university

output:
uiestnvriy
#----------------------
input:
3
sysaeorefvul #<---測資給錯吧!(給相反了,輸出應為輸入,而輸入應為輸出)

output:
saveyourself #sefyaoevlsru
#----------------------
input:
2
cmueoptr  #<---測資給錯吧! 給相反了,輸出應為輸入,而輸入應為輸出)

output:
computer  #cuotmepr
#----------------------
'''
