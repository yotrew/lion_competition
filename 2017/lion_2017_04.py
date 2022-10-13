'''
2018來恩盃:第 4 題 – 六合彩港號台號轉換

Author:Yotrew Wing
https://github.com/yotrew/lion_competition
2022/10/11
'''
nums=list(map(int,input().split(" ")))
nums.sort()

for i in range(len(nums)-1):
    print(nums[i]%10*10+nums[i+1]%10,end=" ")
print(nums[-3]%10*100+nums[-2]%10*10+nums[-1]%10)
'''
input:
17 37 33 12 25 18

output:
27 78 85 53 37 537
'''
