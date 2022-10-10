'''
2019來恩盃:第 2 題 – 字串解碼
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew

用stack:2個stack,一個存重覆數,一個存字串
'''
in_s=input()
str_stack=[]
mul_stack=[]
out_str=""

for i in in_s:
    if 48<=ord(i)<=57: #數字
        mul_stack.append(int(i))
        continue
    if i=="]": #遇右[括號
        x=str_stack.pop()
        str_tmp=""
        while x!="[":#從stack中取到[為止
            str_tmp=x+str_tmp
            x=str_stack.pop()
        y=mul_stack.pop()
        str_stack.append(str_tmp*y) #
        continue
    str_stack.append(i)

while len(str_stack)>1:
    x=str_stack.pop()
    str_stack.append(str_stack.pop()+x)

print(str_stack[-1])
#print(mul_stack)
    
'''
input:
ab2[c]ba 
output:
abccba

input:
3[abc]
output:
abcabcabc

input:
2[a2[b]3[c]] 
output:
abbcccabbccc
'''
