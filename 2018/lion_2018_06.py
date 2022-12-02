'''
2018來恩盃:第 6 題 – 親和數
Author:Yotrew Wing
2022/10/10
https://github.com/yotrew/lion_competition

解法:

'''
x,y=map(int,input().split(" "))
x_factor=[1]
y_factor=[1]
for i in range(2,x):
    if x%i==0:
        x_factor.append(i)
for i in range(2,y):
    if y%i==0:
        y_factor.append(i)
#print(x_factor,y_factor,sum(x_factor),sum(y_factor))
if sum(x_factor)==y and sum(y_factor)==x:
    print("true")
else:
    print("false")
'''
input:
284 220

output:
true
#----------------------
input:
10744 10856

output:
true
#----------------------
input:
10856 12345 

output:
false
'''
