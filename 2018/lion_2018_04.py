'''
2019來恩盃:第 2 題 – 字串解碼
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew

用stack:2個stack,一個存op,一個存數值
解法:
使用四則運算中序轉後序法
'''
in_s=input()
stack=[]
op_stack=[]
priority_dict={")":9,"^":2,"*":2,"/":2,"+":1,"-":1,"(":0} #運算子優先權
op="+-*/^()"
tmp_str=""
def opf(o,x,y):
    if o=="*":
        return (x*y)
    if o=="/":
        return (x/y)
    if o=="+":
        return (x+y)
    if o=="-":
        return (x-y)
    if o=="^":
        return (x**y)
    
for i in in_s:
    if i not in op: #不是運算子時,要串成數值
        tmp_str=tmp_str+i
    else:
        if len(tmp_str)>0: 
            stack.append(float(tmp_str))
            tmp_str=""
        if len(op_stack)==0: #op_stack中沒有任何運算子,無法比較優先順序
            op_stack.append(i)
        else:
            #print(op_stack,i,stack,priority_dict[i],priority_dict[op_stack[-1]])
            if i==")":
                while True: #右括號要做到左括號為止
                    #print(op_stack,i,stack)
                    o=op_stack.pop()
                    if o=="(":
                        break
                    y=stack.pop()
                    x=stack.pop()                    
                    stack.append(opf(o,x,y))
                    #stack.append(x)
            elif i!="(" and priority_dict[i]<priority_dict[op_stack[-1]]:
                y=stack.pop()
                x=stack.pop()
                stack.append(opf(op_stack[-1],x,y))
                op_stack.pop()
            if i!=")":
                op_stack.append(i)

if len(tmp_str)>0: #還有多的數值,也就是最後一個,因為最後一個後面沒有運算子
    stack.append(float(tmp_str))
while len(op_stack)>0:
    #print(op_stack,o,stack)
    if len(stack)<=1:
        break
    y=stack.pop()
    x=stack.pop()
    o=op_stack.pop()
    stack.append(opf(o,x,y))   

if len(op_stack)==0:
    print(f"{stack[0]:.2f}")
else:
    print("N/A")
'''
input:
12+(3.4+5*6.2)/3.2 
output:
22.75

input:
5.6*(6.4^3-8)
output:
1423.21

input:
(1234+5678
output:
N/A
'''
