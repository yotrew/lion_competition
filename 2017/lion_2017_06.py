'''
2018來恩盃:第 6 題 – 產品銷售利潤最大化

Author:Yotrew Wing
https://github.com/yotrew/lion_competition
2022/10/11
解法:
多item的背包問題
'''
ins=list(map(int,input().split(",")))
      #第1個是[],是為了對齊(不用)
items=[[],[1,2],[4,40],[24,300],[15,200],[7,100],[7,90],[3,20],[5,50],[5,60],[2,5]]

DP=[0 for i in range(ins[0]+1)]
for i in range(1,len(items)):
    for j in range(ins[i]):
        for k in range(ins[0],items[i][0]-1,-1):
            w=k-items[i][0]
            if (DP[w]+items[i][1])>(DP[k]):
                DP[k]=DP[w]+items[i][1]
print(DP)
print(DP[-1])
'''
input:
10,1,1,0,1,0,1,1,1,0,1

output:
110

#----------------------
input:
15,2,0,1,5,2,1,3,0,1,1 

output:
202

'''
