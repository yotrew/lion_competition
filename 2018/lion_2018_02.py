'''
2018來恩盃:N 進位系統之乘法直式運算
Author:Yotrew Wing
2022/10/10
https://github.com/yotrew
解法:
就計概(or數概)進制轉
'''
#base=list("0123456789ABCDEFGHIJKLMN")
#print(base)
#print([i for i in range(25)])
base=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
nums=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

#合成符號-數值表及反查表
base_dict=dict(zip(base,nums)) 
rev_base_dict=dict(zip(nums,base))

#print(base_dict)
in_s=input().split(" ")
b=int(in_s[0])
x=in_s[1]
y=in_s[2]

#找出數字中的最大值,如果最大值比進制大或等於就Error
max_num=0
for i in x:
    if max_num < base_dict[i]:
        max_num=base_dict[i]
for i in y:
    if max_num < base_dict[i]:
        max_num=base_dict[i]

if max_num>=b:
    print("Error")
else:
    #print(x[1],x[0],y[1],y[0])
    first=(base_dict[x[0]]*base_dict[y[1]]*b+base_dict[x[1]]*base_dict[y[1]])
    second=(base_dict[x[0]]*base_dict[y[0]]*b+base_dict[x[1]]*base_dict[y[0]])*b
    third=first+second

    first_str=""
    second_str=""
    third_str=""
    
    #10進位轉任何進位
    while first>b:
        first_str=rev_base_dict[first%b]+first_str
        first//=b
    if first>0:
        first_str=rev_base_dict[first]+first_str
    while second>b:
        second_str=rev_base_dict[second%b]+second_str
        second//=b
    if second>0:
        second_str=rev_base_dict[second]+second_str
    while third>b:
        third_str=rev_base_dict[third%b]+third_str
        third//=b
    if third>0:
        third_str=rev_base_dict[third]+third_str
    
    print(x,y,first_str,second_str,third_str)
'''
input:
16 38 2E

output:
38 2E 310 700 A10
#----------------------
input:
15 0A 1F

output:
Error
#----------------------
input:
20 IJ AJ
output:
IJ AJ I01 99A0 A7A1

'''
