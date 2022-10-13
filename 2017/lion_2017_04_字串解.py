'''
2018來恩盃:第 4 題 – 六合彩港號台號轉換

Author:Yotrew Wing
https://github.com/yotrew/lion_competition
2022/10/11
解法:
方法1. 讀入後轉數字,排序,再轉回字串
方法2. 直接使用字串排序(應該不會有問題,排序方式一個字元一個字元比)
'''
#方法1
#nums=list(map(int,input().split(" ")))
#nums.sort()
#nums=list(map(str,nums))

#方法2
nums=input().split(" ")
nums.sort()

for i in range(len(nums)-1):
    print(nums[i][1]+nums[i+1][1],end=" ")
print(nums[-3][1]+nums[-2][1]+nums[-1][1])
'''
input:
17 37 33 12 25 18

output:
27 78 85 53 37 537


'''
