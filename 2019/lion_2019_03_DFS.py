'''
2019來恩盃:第 3 題 – 第 3 題 – ３×３數字推盤(八方塊遊戲)
Author:Yotrew Wing
2022/10/16
https://github.com/yotrew/lion_competition
#N-puzzle game

012
345
678

pos(4)+1=5 right
pos(4)-1=3 left
pos(4)+3=5 down
pos(4)-3=1 up

#DFS的問題是不知道誰是最短,要走過所有才知道,BFS就第一個找到就會是最短
#但DFS/BFS找不到時都會很慢
'''
import copy
import time
found_cnt=32
table=[]
found=False
def DFS(t,pos,cnt,prev):
    global found,found_cnt
    #if found:
    #    return
    
    if cnt>=found_cnt: #加速,找到至少某一步數之後,不可能比這個步數還要多
        return
    #f=True
    #print(t,pos,cnt,prev)
    for i in range(len(t)):
        if t[i]!=i:
            #f=False
            break
    else:
        found=True
        if found_cnt>cnt:
            found_cnt=cnt
        #print("found2:",found,cnt)

    '''if f: #找到
        found=True
        found_cnt=cnt
        print("found2:",found,cnt)
        return found'''
    
    if (pos+1)%3!=0 and prev!=(pos+1): #right
        t1=copy.deepcopy(t)
        t1[pos],t1[pos+1]=t1[pos+1],t1[pos]
        DFS(t1,pos+1,cnt+1,pos)
    if (pos-1)%3!=2 and prev!=(pos-1): #left
        t1=copy.deepcopy(t)
        t1[pos],t1[pos-1]=t1[pos-1],t1[pos]
        DFS(t1,pos-1,cnt+1,pos)
    if not (pos+3)>=9 and prev!=(pos+3): #down
        t1=copy.deepcopy(t)
        t1[pos],t1[pos+3]=t1[pos+3],t1[pos]
        DFS(t1,pos+3,cnt+1,pos)
    if not (pos-3)<=-1 and prev!=(pos-3): #up
        t1=copy.deepcopy(t)
        t1[pos],t1[pos-3]=t1[pos-3],t1[pos]
        DFS(t1,pos-3,cnt+1,pos)
    #print("-"*20)
        
table=list(map(int,input().split()))
print(table)
# 開始測量
start = time.time()
start_pos=-1
for i in range(len(table)):
    if table[i]==0:
        start_pos=i
DFS(table.copy(),start_pos,0,-1)
if found_cnt<32:
    print(found_cnt,found)
else:
    print(-1)

# 結束測量
end = time.time()
# 輸出結果
print("執行時間：%f 秒" % (end - start))
'''
input:
1 4 2 0 3 5 6 7 8
output:
3

input:
6 3 5 7 1 0 4 2 8
output:
15

input:
8 7 6 0 4 1 2 5 3
output:
31

input:
7 2 0 5 4 6 8 3 1 
output:
-1
'''
