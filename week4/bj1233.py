import sys

S1, S2, S3=sys.stdin.readline().split()

S1=int(S1)
S2=int(S2)
S3=int(S3)

sum=[]

for _ in range(S1+S2+S3):
	sum.append(0)
	
	
for a in range(S1):
    for b in range(S2):
        for c in range(S3):
            sum[a+b+c]+=1

big_num=[0,-1]
			
for i in range(len(sum)):
    if big_num[0]<sum[i]:
        big_num[0]=sum[i]
        big_num[1]=i

print(big_num[1]+3)