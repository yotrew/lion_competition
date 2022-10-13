'''
2018來恩盃:第 5 題 – 最長不重複的英文子字串

Author:Yotrew Wing
https://github.com/yotrew/lion_competition
2022/10/11
解法:
暴力解,找出任一區段,從這個區段挑任一個字元來比對,若挑出來的字元與它位置不符就是有重複
'''
ins=input()
max_cnt=0
max_str=[]
for i in range(0,len(ins)):#因為要找出第一個最長的,所以從最左邊最短開始
    for j in range(1,len(ins)+1):
        tmp=ins[i:j]
        flag=True
        for k in range(len(tmp)):
            for l in range(len(tmp)):
                if tmp[l]==tmp[k]:
                    break
            if k!=l:
                flag=False
                break
        if flag==True and max_cnt<(j-i):
            max_cnt=j-i
            max_str=ins[i:j]
            
    
print(f"{max_str} {max_cnt}")
'''
input:
abcdabcdbb

output:
abcd 4

#----------------------
input:
dddd

output:
d 1
#----------------------
input:
pwwkew

output:
wke 3

'''
