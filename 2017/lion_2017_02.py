'''
2018來恩盃:第 2 題 – 車輛平均油耗

Author:Yotrew Wing
https://github.com/yotrew/lion_competition
2022/10/11

#只有一列輸入??
'''
xn=list(map(float,input().split(" ")))
sum1=0
for i in range(len(xn)-1):
    sum1+=xn[i]
    print(f"{(sum1/(i+1)):.2f}",end=" ")
print()
'''
input:
12.34 11.56 13.45 0

output:
12.34 11.95 12.45
#----------------------
input:
15.60 18.91 16.73 14.37 0

output:
15.60 17.25 17.08 16.40
'''
