'''
2018來恩盃:第 3 題 – 雷射打點座標轉換

Author:Yotrew Wing
https://github.com/yotrew/lion_competition
2022/10/13
解法:
用旋轉座標解
'''
import math
c1,c2,a1,a2,b1,b2=map(float,input().split(","))
A1=0
A2=0
B1=500
B2=0
#把新A點移回原來的(A1.A2)有多遠?距離a_dx和a_dy(以A點為基準點做旋轉)
a_dx=a1-A1 
a_dy=a2-A2
#A移回原來的(0,0)後,b點也要跟著移
new_bx=b1-a_dx
new_by=b2-a_dy

#求出移動後A~B線段與(A1,A2)~(B1.B2)的夾角為多少
if new_bx==0: #若新的b點,x坐標為0,代表90度
    angle=math.pi/2  #pi是180度,pi/2=>90度
else:#不是就使用反正切函數atan求角度
    angle=math.atan(new_by/new_bx)

#求出旋轉角度後,就可求出新的(c1,c2),但這是把A點移回(A1,A2)的結果,所以要再移回去 +a_dx,+a_dy
#Refhttps://silverwind1982.pixnet.net/blog/post/165223625-%E6%97%8B%E8%BD%89%E7%9F%A9%E9%99%A3-%28rotation-matrix%29
cx2 =math.cos(angle)*c1-math.sin(angle)*c2
cy2 =math.sin(angle)*c1+math.cos(angle)*c2
#移回去
cx2=cx2+a_dx
cy2=cy2+a_dy

print(f"{cx2:.4f} {cy2:.4f}")    
    
'''
input:
300,500,50,50,550,50

output:
350.0000,550.0000
#----------------------
input:
300,500,50,50,548.0973,93.5779 

output:
305.2805,574.2441
'''
