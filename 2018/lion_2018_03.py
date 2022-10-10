'''
2018來恩盃:第 3 題 – 資料傳輸編碼
Author:Yotrew Wing
2022/10/10
https://github.com/yotrew
解法:

'''
import math
in_s=input().split(" ")
m=int(in_s[0])
#in_data=list(map(int,in_s[1]))
in_data=in_s[1] #沒有要做運算,所以不用轉int
#print(in_data)
k=int(math.log(m,2))+1 #用內建套件的log或是用迴圈找出2^k > l
#print(k)
cnt=0
out_data=[0 for i in range(m+k)]
xor_data=0 #0和某數xor還是某數
for i in range(m+k):
    if (i+1)==2**cnt:
        cnt+=1
        continue
    #print(i,i-cnt)
    if in_data[i-cnt]=="1": #那個位元為1時要做xor
        '''if xor_data==None:
            xor_data=(i+1)
        else:
            xor_data^=(i+1)

        '''
        xor_data^=(i+1)
        #print(xor_data)
    out_data[i]=in_data[i-cnt]
bin_xor_data=bin(xor_data)[-1:-(k+1):-1]
#print(bin_xor_data[-1:-5:-1])
for i in range(k):
    #out_data[2**i-1]=int(bin_xor_data[i])
    out_data[2**i-1]=bin_xor_data[i]
print("".join(out_data))
'''
input:
8 11000010

output:
101110010010
#----------------------
input:
8 10101101 

output:
011001011101
'''
