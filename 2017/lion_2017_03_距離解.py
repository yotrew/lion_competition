'''
2018來恩盃:第 3 題 – 雷射打點座標轉換

Author:Yotrew Wing
https://github.com/yotrew/lion_competition
2022/10/11
解法1:
暴力解,使用距離公式,旋轉距離不會變,應該只會有2組解,一組正解,一組是長方形面板上方鏡射的解
先大跨距求,接近後再小跨距求
'''
import math
import time


c1,c2,a1,a2,b1,b2=map(float,input().split(","))

# 開始測量
start = time.time()


A1=0
A2=0
B1=500
B2=0
ac=((A1-c1)**2+(A2-c2)**2)**0.5 #原先A->C距離
bc=((B1-c1)**2+(B2-c2)**2)**0.5 #原先B->C距離
x_shift=max(abs(A1-a1),abs(B1-b1)) #x位移最大值
y_shift=max(abs(A2-a2),abs(B2-b2)) #y位移最大值

flag=0
cx2=c1
cy2=c2
print(cx2,cy2)
step=10
step2=1000
for cx in range(int(c1-x_shift-1)*step,int(c1+x_shift+1)*step+1):
    for cy in range(int(c2-y_shift-1)*step,int(c2+y_shift+1)*step+1):
        ac2=((a1-cx/step)**2+(a2-cy/step)**2)**0.5 #新A->C距離
        bc2=((b1-cx/step)**2+(b2-cy/step)**2)**0.5 #新B->C距離
        if abs(ac2-ac)<=0.05 and abs(bc2-bc)<=0.05:
            flag=1
            cx2=cx
            cy2=cy

            for cx_t in range(cx2*step2-step2//2,cx2*step2+step2//2):
                for cy_t in range(cy2*step2-step2//2,cy2*step2+step2//2):
                    ac2=((a1-cx_t/(step*step2))**2+(a2-cy_t/(step*step2))**2)**0.5 #新A->C距離
                    bc2=((b1-cx_t/(step*step2))**2+(b2-cy_t/(step*step2))**2)**0.5 #新B->C距離
                    #print(ac,ac2,bc,bc2,abs(ac2-ac),(bc2-bc))
                    if abs(ac2-ac)<=0.00001 and abs(bc2-bc)<=0.00001:
                        print("test:",cx_t,cy_t)
                        flag=2
                        cx2=cx_t
                        cy2=cy_t
                        break
            break
    if flag==2:
        break
if flag==2:
    print(f"{cx2/step/step2:.4f} {cy2/step/step2:.4f}")
else:
    print("找不到???") #<--不應該出現
print("finished")     


# 結束測量
end = time.time()
# 輸出結果
print("執行時間：%f 秒" % (end - start))
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
