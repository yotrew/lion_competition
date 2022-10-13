'''
2018來恩盃:第 5 題 – 最長不重複的英文子字串

Author:Yotrew Wing
https://github.com/yotrew/lion_competition
2022/10/11
解法:
用set來解,如果取出來的set長度不等於原先長度就代表有重複
'''
ins=list(input())
max_cnt=0
max_str=[]
for i in range(0,len(ins)):#因為要找出第一個最長的,所以從最左邊最短開始
    for j in range(1,len(ins)+1):
        tmp=set(ins[i:j])
        if len(tmp)==(j-i) and  len(tmp)>max_cnt:
            #print(len(tmp),ins[i:j],tmp)
            max_cnt=len(tmp)
            max_str=ins[i:j].copy()
    
    
print(f"{''.join(max_str)} {max_cnt}")
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
