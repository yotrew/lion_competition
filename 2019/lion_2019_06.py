'''
2019來恩盃:第 6 題 – 行程長度編碼與解碼
Author:Yotrew Wing
2022/10/09
https://github.com/yotrew
'''
in_s=input()
prev=""
cnt=0
for i in in_s:
    if i==prev:
        cnt+=1
    else:
        if cnt>0:
            print(f"{cnt}{prev}",end="")
        prev=i
        cnt=1
if cnt>0:
    print(f"{cnt}{prev}")
else:
    print()
        
'''
範例測資
Input:
AAAABBBCCDEEEE
Output:
4A3B2C1D4E
Input:
YYBBCC 2Y2B2C
額外測資
Input: 
AAAACCBDE
Output:
4A2C1B1D1E

Input:
AAABBB
Output:3A3B

Input:
DDDDAAACCFFFBBA
Output:
4D3A2C3F2B1A

'''
