'''
2018來恩盃:第 4 題 – 計算機程式
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew/lion_competition

解法:
直接用eval
'''
in_s=input().replace("^","**")
try:
    print(f"{(eval(in_s)):.2f}")
except:
    print(f"N/A")
'''
input:
12+(3.4+5*6.2)/3.2 
output:
22.75

input:
5.6*(6.4^3-8)
output:
1423.21

input:
(1234+5678
output:
N/A
'''
