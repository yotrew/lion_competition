'''
2020來恩盃:第 5 題 找出可能的鈍角三角形的最長周長
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew

鈍角三角形:a^2+b^2<c^2
銳角三角形:a^2+b^2>c^2
直角三角形:a^2+b^2=c^2
三角形:a+b>c

解法:
a一定是輸入資料的最小值,c一定是輸入資料的最大值,只須找b

解法2:
若直接a是最小值, b,c最大值2個,答案會對嗎?(會有測資造成此條件錯誤嗎?)
'''

n=int(input())
edge=list(map(int,input().split(" ")))
edge.sort()
#print(edge)
a=edge[0]
c=edge[-1]

for i in range(len(edge)-2,0,-1): #n-1~1,因為要找最大值,所以b從最後倒數第2個開始
    b=edge[i]
    #print(a,b,c,a**2,b**2,c**2,(a+b+c))
    if a**2+b**2<c**2:
        print(a+b+c)
        break
else:#for迴圈執行到最後
    print(0)
'''
#其他程式語言寫法
n=int(input())
edge=list(map(int,input().split(" ")))
edge.sort()
#print(edge)
a=edge[0]
c=edge[-1]
flag=True
for i in range(len(edge)-2,0,-1): #n-1~1
    b=edge[i]
    #print(a,b,c,a**2,b**2,c**2,(a+b+c))
    if a**2+b**2<c**2:
        print(a+b+c)
        flag=False
        break
if flag:
    print(0)

'''
'''
input:
4
56 112 84 137

output:
305

input:
5
56 57 55 58 56


output:
0
'''
