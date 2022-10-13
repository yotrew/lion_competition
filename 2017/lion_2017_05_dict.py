'''
2018來恩盃:第 5 題 – 最長不重複的英文子字串

Author:Yotrew Wing
https://github.com/yotrew/lion_competition
2022/10/11
解法:
用dictionary來統計
'''
ins=list(input())
stat=dict()
for i in ins:
    stat[i]=0
#print(stat)
max_cnt=0
max_str=[]
for i in range(0,len(ins)):#因為要找出第一個最長的,所以從最左邊最短開始
    for j in range(1,len(ins)+1):
        tmp=ins[i:j]
        stat_tmp=stat.copy()
        flag=True
        for k in tmp:
            stat_tmp[k]+=1
            if stat_tmp[k]>=2:
                flag=False
                break
        if flag==True and max_cnt<(j-i):
            #print(tmp,i,j,stat_tmp,flag)
            max_cnt=j-i
            max_str=tmp.copy()
        
    
    
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
