'''
2018來恩盃:第 1 題 – 運算排列組合

Author:Yotrew Wing
https://github.com/yotrew/lion_competition
2022/10/11
#共有288種組合,怎麼寫的完...只能偷懶用eval
'''
oprand=list(input().split(" "))
expression=['',"",'+','',"",'','+',"",'']
#expression=['',a,'+','',b,'','+',c,'']
op=['+','-','*','/']
brackets=[["(",")"],["",""]] #有括號跟沒括號
cnt=0 #統計有多少種組合
flag=True #是否有找到
outflag=True
for a in oprand:
    for b in oprand:
        for c in oprand:
            if a==b or a==c or b==c:
                continue
            for i in op:
                for j in op:
                    for k in brackets:
                        for l in brackets:
                            if k[0]=="(" and l[0]=="(":
                                continue
                            expression[1]=a
                            expression[4]=b
                            expression[7]=c
                            expression[0]=k[0]
                            expression[5]=k[1]
                            expression[2]=i
                            expression[6]=j
                            expression[3]=l[0]
                            expression[8]=l[1]
                            ex_str="".join(expression)
                            cnt+=1
                            if eval(ex_str)==16:
                                if outflag: #是否已輸出答案,只是為了統計組合數目
                                    print(ex_str+"=16")
                                    outflag=False
                                flag=False
print(cnt)
if flag:
    print("None")
'''
input:
1 3 5

output:
(5*3)+1=1  #<--任一算式
#----------------------
input:
6 8 1

output:
None

'''
