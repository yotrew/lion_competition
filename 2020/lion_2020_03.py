'''
2020來恩盃:第 3 題 以遞增取數由一亂數數列取出最多個整數
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew

本題題意不好理解
本題題意是說由左自右取,右邊比上一個取的"大"才能取,比上一個取還要"小"就跳過,取到最後一個

解法:
最長遞增子序列(ongest Increasing Subsequence,LIS)
'''
n=int(input())
nums=list(map(int,input().split(" ")))
nums_l=len(nums)
dp=[0 for i in range(n+1)]


for i in range(nums_l):
    for j in range(i):
        #print(i,j)
        if nums[i]>nums[j] and dp[j]+1>dp[i]:
            dp[i]=dp[j]+1
    
print(dp)
print(max(dp)+1) #要加上自己本身
        
'''
input:
5
1 2 3 4 3
output:
4

input:
20
10 12 30 14 36 18 20 25 48 32 79 21 49 78 98 22 1 99 97 2

output:
11
'''
