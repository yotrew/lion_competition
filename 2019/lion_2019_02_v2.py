'''
2019來恩盃:第 2 題 – 字串解碼
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew

使用for迴圈找[]來模擬stack動作
'''
in_s=input()
cnt=0
i=0
while i<len(in_s):
    if 48<=ord(in_s[i])<=57: #數字
        start=0
        end=0
        for j in range(len(in_s)):
            if in_s[j]=="[":
                start=j+1
                break
        for j in range(len(in_s)):
            if in_s[j]=="[":
                cnt+=1
            if in_s[j]=="]":
                cnt-=1
                
                if cnt==0:
                    end=j-1
                    break
        in_s=in_s[0:start-2]+int(in_s[i])*(in_s[start:end+1])+in_s[end+2:]
    i+=1

    
print(in_s,end="")
    
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
