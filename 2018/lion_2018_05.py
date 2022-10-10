'''
2018來恩盃:第 5 題 – Karatsuba 遞迴乘法
Author:Yotrew Wing
2022/10/10
解法:
Karatsuba演算法

https://github.com/yotrew
'''
import math
def Karatsuba(x,y):
    
    n=max(int(math.log(x,10)),int(math.log(x,10)))+1
    print(f"x={x}, y={y}")
    if x<10 or y<10:
        return x*y
    
    a=x//(10**(n//2))
    b=x%(10**(n//2))
    c=y//(10**(n//2))
    d=y%(10**(n//2))

    #= a∗c∗10^n + (a∗d + b∗c) ∗ 10^(n/2)+b*d
    #= 計算式1∗10^n + 計算式4∗10^(n/2) + #計算式2
    z2=Karatsuba(a,c) #計算式1
    z0=Karatsuba(b,d) #計算式2
    z1=Karatsuba(a+b,c+d) #計算式3
                            #計算式4(=3-2-1)
    return z2*10**(n//2*2)+(z1-z2-z0)*10**(n//2) +z0

x,y=map(int,input().split(" "))
p=Karatsuba(x,y)
print("result:",p,x*y)
'''
input:
12 34

output:
x=12, y=34
x=1, y=3
x=2, y=4
x=3, y=7
408
#----------------------
input:
123 45

output:
x=123, y=45
x=12, y=4
x=3, y=5
x=15, y=9
5535
#----------------------
input:
987 123

output:
x=987, y=123
x=98, y=12
x=9, y=1
x=8, y=2
x=17, y=3
x=7, y=3
x=105, y=15
x=10, y=1
x=5, y=5
x=15, y=6
121401
'''
