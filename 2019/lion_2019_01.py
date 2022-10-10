'''
2019來恩盃:第 1 題 – 正整數最大公因數及最小公倍數
Author:Yotrew Wing
2022/10/10
https://github.com/yotrew

3數的GCD(最大公因數)=先2數之最大公因數,再與第3數求最大公因數=GCD(GCD(a,b),c)
2數的LCM(最小公倍數)= a*b/GCD(a,b)
3數的LCM(最小公倍數)=先求2數的最小公倍數,再與第3數求最小公倍數
再與第3數求最小公倍數-->2數的最小公倍數的數要與第3數先取GCD
'''
def GCD(a,b):
    r=a%b
    if r==0:
        return b
    else:
        return GCD(b,r)
    
a,b,c=map(int,input().split(" "))
gcd1=GCD(a,b)
gcd2=GCD(gcd1,c)
print(f"GCD={gcd2}")
lcm1=(a*b/gcd1) 
gcd3= GCD(lcm1,c) 
#print(lcm1,gcd3,c)
LCM=int((lcm1*c)//gcd3)
print(f"LCM={LCM}")
    
'''
input:
60 120 72 
output:
GCD=12
LCM=360
'''
