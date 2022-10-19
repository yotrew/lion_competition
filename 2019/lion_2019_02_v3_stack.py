'''
2019來恩盃:第 2 題 – 字串解碼
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew
用stack
'''
in_s=input()
stack=[]
out_str=""

for i in in_s:
    if i=="]": #遇右]括號
        str_tmp=""
        while True:
            x=stack.pop()
            if x=="[":
                str_tmp=str_tmp*int(stack.pop())#左[括之前一定是數字(重複次數),在Python直接用*
                break
            str_tmp=x+str_tmp
        stack.append(str_tmp) #
        continue
    stack.append(i)

#在Python中可以直接用print("".join(stack)).其他程式語言就照stack做法
while len(stack)>1:
    x=stack.pop()
    y=stack.pop()
    stack.append(y+x)
print(stack[-1])

#print("".join(stack))
    
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
